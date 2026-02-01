"""Fix Unicode ordering in qr_*.py files to match preferred order.

Preferred order per copilot-instructions.md:
base letter → shin/sin dot → dagesh → rafeh → vowels → meteg → accents
"""

import os
import re

def get_mark_order(cp):
    """Get sort order for a Hebrew combining mark."""
    # Shin/sin dots: U+05C1, U+05C2
    if cp in (0x05C1, 0x05C2):
        return 1
    # Dagesh: U+05BC
    if cp == 0x05BC:
        return 2
    # Rafeh: U+05BF
    if cp == 0x05BF:
        return 3
    # Vowels: U+05B0-U+05BB, U+05C7
    if 0x05B0 <= cp <= 0x05BB or cp == 0x05C7:
        return 4
    # Meteg: U+05BD
    if cp == 0x05BD:
        return 5
    # Accents (cantillation): U+0591-U+05AF
    if 0x0591 <= cp <= 0x05AF:
        return 6
    return 99  # Other (punctuation, letters, etc.)

def is_combining_mark(cp):
    """Check if codepoint is a Hebrew combining mark."""
    order = get_mark_order(cp)
    return 1 <= order <= 6

def reorder_hebrew_string(text):
    """Reorder combining marks in a Hebrew string to match preferred order."""
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        cp = ord(ch)
        
        # Check if this is a base character (letter or punctuation)
        if not is_combining_mark(cp):
            result.append(ch)
            i += 1
            
            # Collect all combining marks after this character
            marks = []
            while i < len(text):
                ch2 = text[i]
                cp2 = ord(ch2)
                if is_combining_mark(cp2):
                    marks.append((get_mark_order(cp2), ch2))
                    i += 1
                else:
                    break
            
            # Sort marks by preferred order and append
            marks.sort(key=lambda x: x[0])
            for _, mark_ch in marks:
                result.append(mark_ch)
        else:
            # Orphan combining mark (shouldn't happen in well-formed text)
            result.append(ch)
            i += 1
    
    return ''.join(result)

def fix_file(filepath):
    """Fix Unicode ordering in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Find all quoted strings containing Hebrew and fix them
    def fix_match(match):
        s = match.group(1)
        fixed = reorder_hebrew_string(s)
        return f'"{fixed}"'
    
    # Match strings in quotes that contain Hebrew characters
    pattern = r'"([^"]*[\u0590-\u05FF][^"]*)"'
    content = re.sub(pattern, fix_match, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    qr_dir = 'pyauthor_qr'
    fixed_files = []
    
    for filename in sorted(os.listdir(qr_dir)):
        if filename.startswith('qr_') and filename.endswith('.py'):
            filepath = os.path.join(qr_dir, filename)
            if fix_file(filepath):
                fixed_files.append(filename)
    
    if fixed_files:
        print(f"Fixed Unicode ordering in {len(fixed_files)} files:")
        for f in fixed_files:
            print(f"  {f}")
    else:
        print("No files needed fixing.")

if __name__ == '__main__':
    main()

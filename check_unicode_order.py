"""Check Unicode ordering in qr_*.py files against preferred order.

Preferred order per copilot-instructions.md:
base letter → shin/sin dot → dagesh → rafeh → vowels → meteg → accents
"""

import os
import re
import unicodedata

# Unicode ranges for Hebrew marks
# Based on https://unicode.org/charts/PDF/U0590.pdf

def get_mark_category(cp):
    """Categorize a Hebrew combining mark by its position in the preferred order."""
    # Shin/sin dots: U+05C1, U+05C2
    if cp in (0x05C1, 0x05C2):
        return 1, "shin/sin dot"
    # Dagesh: U+05BC
    if cp == 0x05BC:
        return 2, "dagesh"
    # Rafeh: U+05BF
    if cp == 0x05BF:
        return 3, "rafeh"
    # Vowels: U+05B0-U+05BB, U+05C7
    if 0x05B0 <= cp <= 0x05BB or cp == 0x05C7:
        return 4, "vowel"
    # Meteg: U+05BD
    if cp == 0x05BD:
        return 5, "meteg"
    # Accents (cantillation): U+0591-U+05AF
    if 0x0591 <= cp <= 0x05AF:
        return 6, "accent"
    # Other punctuation
    if 0x05BE <= cp <= 0x05C0 or cp == 0x05C3 or cp == 0x05C6:
        return 99, "punctuation"
    # Base letters
    if 0x05D0 <= cp <= 0x05EA:
        return 0, "letter"
    # Final forms
    if 0x05DA <= cp <= 0x05DF:
        return 0, "letter"
    return -1, "other"

def check_order(text, context=""):
    """Check if combining marks follow the preferred order after each base letter."""
    issues = []
    i = 0
    while i < len(text):
        ch = text[i]
        cp = ord(ch)
        cat, cat_name = get_mark_category(cp)
        
        if cat == 0:  # Base letter
            base_letter = ch
            base_idx = i
            marks = []
            i += 1
            # Collect all combining marks after this letter
            while i < len(text):
                ch2 = text[i]
                cp2 = ord(ch2)
                cat2, cat_name2 = get_mark_category(cp2)
                if cat2 == 0 or cat2 == 99 or cat2 == -1:
                    # Next base letter or punctuation or other
                    break
                marks.append((cp2, cat2, cat_name2, ch2))
                i += 1
            
            # Check order of marks
            if len(marks) > 1:
                for j in range(len(marks) - 1):
                    _, order1, name1, ch1 = marks[j]
                    _, order2, name2, ch2 = marks[j+1]
                    if order1 > order2:
                        issues.append({
                            'base': base_letter,
                            'base_cp': f"U+{ord(base_letter):04X}",
                            'problem': f"{name1} (U+{ord(ch1):04X}) before {name2} (U+{ord(ch2):04X})",
                            'marks': [(f"U+{m[0]:04X}", m[2]) for m in marks],
                            'context': context
                        })
                        break
        else:
            i += 1
    
    return issues

def extract_hebrew_strings(filepath):
    """Extract Hebrew strings from a Python file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all quoted strings containing Hebrew
    strings = []
    # Match strings in quotes that contain Hebrew characters
    pattern = r'"([^"]*[\u0590-\u05FF][^"]*)"'
    for match in re.finditer(pattern, content):
        strings.append(match.group(1))
    return strings

def main():
    qr_dir = 'pyauthor_qr'
    all_issues = []
    
    for filename in sorted(os.listdir(qr_dir)):
        if filename.startswith('qr_') and filename.endswith('.py'):
            filepath = os.path.join(qr_dir, filename)
            hebrew_strings = extract_hebrew_strings(filepath)
            
            for s in hebrew_strings:
                issues = check_order(s, f"{filename}: {s}")
                all_issues.extend(issues)
    
    if all_issues:
        print(f"Found {len(all_issues)} Unicode ordering issues:\n")
        for issue in all_issues:
            print(f"File context: {issue['context']}")
            print(f"  Base letter: {issue['base']} ({issue['base_cp']})")
            print(f"  Problem: {issue['problem']}")
            print(f"  Mark order: {issue['marks']}")
            print()
    else:
        print("No Unicode ordering issues found!")

if __name__ == '__main__':
    main()

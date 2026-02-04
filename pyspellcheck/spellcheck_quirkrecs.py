"""
Spell check English strings in quirkrecs.json

Usage:
    python pyspellcheck/spellcheck_quirkrecs.py

Requires: pip install pyspellchecker
"""

import json
import re
from pathlib import Path
from spellchecker import SpellChecker


def load_custom_dictionary(dict_path: Path) -> tuple[set[str], list[str]]:
    """Load custom words and phrases from dictionary file.
    
    Returns (words, phrases) where phrases are multi-word entries.
    """
    words = set()
    phrases = []
    if dict_path.exists():
        for line in dict_path.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                if ' ' in line:
                    phrases.append(line)
                else:
                    words.add(line.lower())
    return words, phrases


def extract_english_words(text: str) -> list[str]:
    """Extract English words from text, ignoring Hebrew and sigla."""
    # Remove Hebrew characters (includes base letters, vowel points, accents, marks)
    text = re.sub(r'[\u0590-\u05FF]+', ' ', text)
    # Remove $-prefixed sigla ($BHQ, $yod, $BHL_A, etc.)
    text = re.sub(r'\$[A-Za-z_]+', ' ', text)
    # Extract words (letters including scholarly transliteration chars like š, ṣ, ḥ)
    # Include typographic apostrophe (') as part of contractions
    # Include μ for sigla like μL, μA
    words = re.findall(r"[a-zA-ZšṣḥŠṢḤμ]+(?:'[a-zA-Z]+)?", text)
    return words


# Fields that contain English prose to spell-check
PROSE_FIELDS = {
    'qr-bhq-comment',
    'qr-generic-comment', 
    'qr-what-is-weird',
}


def check_spelling(quirkrecs_path: Path, custom_dict_path: Path):
    """Check spelling of English words in quirkrecs.json."""
    spell = SpellChecker()
    custom_words, custom_phrases = load_custom_dictionary(custom_dict_path)
    
    with open(quirkrecs_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    issues = []
    
    for rec in data:
        rec_id = rec.get('qr-id', 'unknown')
        
        # Check prose fields only
        for key, value in rec.items():
            if key not in PROSE_FIELDS:
                continue
            if isinstance(value, str):
                text = value
                # Remove accepted phrases before word extraction
                for phrase in custom_phrases:
                    text = re.sub(re.escape(phrase), ' ', text, flags=re.IGNORECASE)
                words = extract_english_words(text)
                for word in words:
                    word_lower = word.lower()
                    if word_lower not in custom_words and word_lower not in spell:
                        issues.append({
                            'record': rec_id,
                            'field': key,
                            'word': word,
                            'suggestions': list(spell.candidates(word_lower) or [])[:5]
                        })
    
    return issues


def main():
    project_root = Path(__file__).parent.parent
    quirkrecs_path = project_root / 'out' / 'quirkrecs.json'
    custom_dict_path = Path(__file__).parent / 'custom_dictionary.txt'
    
    if not quirkrecs_path.exists():
        print(f"Error: {quirkrecs_path} not found")
        print("Run: python main_gen_misc_authored_english_documents.py")
        return
    
    print(f"Checking spelling in {quirkrecs_path}...")
    print(f"Using custom dictionary: {custom_dict_path}")
    issues = check_spelling(quirkrecs_path, custom_dict_path)
    
    if issues:
        print(f"\nFound {len(issues)} potential spelling issues:\n")
        for issue in issues:
            print(f"  [{issue['record']}] {issue['field']}: '{issue['word']}'")
            if issue['suggestions']:
                print(f"    Suggestions: {', '.join(issue['suggestions'])}")
        
        # Group by word
        word_counts = {}
        for issue in issues:
            word = issue['word'].lower()
            word_counts[word] = word_counts.get(word, 0) + 1
        
        print("\n--- Summary by word ---")
        for word, count in sorted(word_counts.items(), key=lambda x: -x[1]):
            print(f"  {word}: {count} occurrence(s)")
    else:
        print("\nNo spelling issues found!")


if __name__ == '__main__':
    main()

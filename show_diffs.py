"""Show character-by-character comparison of consensus vs proposed values."""

import unicodedata

# Data extracted from git diff
changes = [
    ("qr_0627", "עַֽל־רֵיעֲכֶֽם׃", "עַל־רֵֽיעֲכֶֽם׃"),
    ("qr_0720", "הָ֫אָדָ֥ם", "הָאָ֫דָ֥ם"),
    ("qr_0802", "כַּ֝בִּ֗יר", "כַּ֝בִּיר"),
    ("qr_1209", "יַד־יְ֝הֹוָ֗ה", "יַד־יְ֝הֹוָה"),
    ("qr_1606", "מַה־מִּנִּ֥י", "מַה־מִנִּ֥י"),
    ("qr_1703", "עׇרְבֵ֣נִי", "עַרְבֵ֣נִי"),
    ("qr_2001", "הַֽנַּעֲמָתִ֗י", "הַנַּֽעֲמָתִ֗י"),
    ("qr_2107", "מַ֭דּוּעַ", "מַ֣דּוּעַ"),
    ("qr_2115", "מַה־שַּׁדַּ֥י", "מַה־שַׁדַּ֥י"),
    ("qr_2210", "וִ֝יבַהֶלְךָ֗", "וִ֝יבַהֶלְךָ"),
    ("qr_2224", "וּכְצ֖וּר", "וּבְצ֖וּר"),
    ("qr_2413", "בְּֽמֹרְדֵ֫י א֥וֹר", "בְֽמֹרְדֵ֫י־א֥וֹר"),
    ("qr_2418", "לֹא־יִ֝פְנֶ֗ה", "לֹא־יִ֝פְנֶה"),
    ("qr_2709", "הֲֽ֭צַעֲקָתוֹ", "הַֽ֭צַעֲקָתוֹ"),
    ("qr_2903", "לְ֝אוֹר֗וֹ", "לְ֝אוֹרוֹ"),
    ("qr_3102", "וּמֶ֤ה", "וּמֶ֤ה |"),
    ("qr_3120", "כְּ֝בָשַׂ֗י", "כְ֝בָשַׂי"),
    ("qr_3211", "הוֹחַ֨לְתִּי ׀", "הוֹחַ֨לְתִּי"),
    ("qr_3328", "וְ֝חַיָּת֗וֹ", "וְ֝חַיָּתוֹ"),
    ("qr_3405", "כִּֽי־אָמַ֣ר", "כִּֽי־אָמַ֭ר"),
    ("qr_3433_A", "הֲֽמֵעִמְּךָ֬", "הַֽמֵעִמְּךָ֬"),
    ("qr_3433_B", "יְשַׁלְּמֶ֨נָּה ׀", "יְשַׁלְמֶ֨נָּה ׀"),
    ("qr_3433_C", "יְשַׁלְּמֶ֨נָּה ׀", "יְשַׁלְּמֶ֨נָּה"),
    ("qr_3433_D", "וּֽמַה־יָּדַ֥עְתָּ", "וּֽמַה־יָדַ֥עְתָּ"),
    ("qr_3437", "יִשְׂפּ֑וֹק", "יִסְפּ֑וֹק"),
    ("qr_3507", "מַה־מִּיָּדְךָ֥", "מַה־מִיָּדְךָ֥"),
    ("qr_3829", "שָׁ֝מַ֗יִם", "שָׁ֝מַיִם"),
    ("qr_3915", "תְדוּשֶֽׁהָ׃", "תְּדוּשֶֽׁהָ׃"),
    ("qr_3925", "שָׂ֝רִ֗ים", "שָׂ֝רִים"),
    ("qr_4019_B", "הָ֝עֹשׂ֗וֹ", "הָ֝עֹשׂוֹ"),
]

# ANSI colors
RED_BG = "\033[41m"
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
RESET = "\033[0m"
BOLD = "\033[1m"

def char_info(ch):
    """Get Unicode info for a character."""
    cp = ord(ch)
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "(unknown)"
    return f"U+{cp:04X} {name}"

def print_comparison(file_id, consensus, proposed):
    """Print character-by-character comparison."""
    print(f"\n{BOLD}{'='*80}{RESET}")
    print(f"{BOLD}{file_id}{RESET}")
    print(f"Consensus: {consensus}")
    print(f"Proposed:  {proposed}")
    print()
    
    # Pad to same length
    max_len = max(len(consensus), len(proposed))
    cons_chars = list(consensus) + [''] * (max_len - len(consensus))
    prop_chars = list(proposed) + [''] * (max_len - len(proposed))
    
    print(f"{'Idx':<4} {'Consensus':<45} {'Proposed':<45}")
    print("-" * 94)
    
    for i, (c1, c2) in enumerate(zip(cons_chars, prop_chars)):
        info1 = char_info(c1) if c1 else "(none)"
        info2 = char_info(c2) if c2 else "(none)"
        
        if c1 != c2:
            # Highlight differences
            display1 = f"{RED_BG}{info1}{RESET}"
            display2 = f"{GREEN_BG}{info2}{RESET}"
        else:
            display1 = info1
            display2 = info2
        
        # Only print if there's a difference or near a difference
        print(f"{i:<4} {display1:<55} {display2:<55}")

def print_diff_only(file_id, consensus, proposed):
    """Print only the differences."""
    print(f"\n{BOLD}{file_id}{RESET}: {consensus} → {proposed}")
    
    max_len = max(len(consensus), len(proposed))
    cons_chars = list(consensus) + [''] * (max_len - len(consensus))
    prop_chars = list(proposed) + [''] * (max_len - len(proposed))
    
    diffs = []
    for i, (c1, c2) in enumerate(zip(cons_chars, prop_chars)):
        if c1 != c2:
            info1 = char_info(c1) if c1 else "(none)"
            info2 = char_info(c2) if c2 else "(none)"
            diffs.append((i, info1, info2))
    
    if diffs:
        print(f"  {'Idx':<4} {RED_BG}Consensus{RESET:<40} {GREEN_BG}Proposed{RESET:<40}")
        for idx, info1, info2 in diffs:
            print(f"  {idx:<4} {RED_BG}{info1}{RESET:<50} {GREEN_BG}{info2}{RESET:<50}")

# Main
print(f"{BOLD}Character-by-character diff: qr-consensus vs qr-lc-proposed{RESET}")
print(f"Legend: {RED_BG}Removed{RESET} / {GREEN_BG}Added{RESET}")

for file_id, consensus, proposed in changes:
    print_diff_only(file_id, consensus, proposed)

print(f"\n{'='*80}")
print("Done!")

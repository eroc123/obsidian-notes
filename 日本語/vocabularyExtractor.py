import MeCab

# Tokenization and parsing function using MeCab
def parse_japanese(text):
    tagger = MeCab.Tagger()
    tagger.parse('')  # Needed to avoid parser errors
    parsed_text = tagger.parse(text)
    return parsed_text.split('\n')[:-2]  # Remove last two elements which are empty strings

# Function to extract verb forms
def extract_verb_forms(parsed_tokens):
    verb_forms = {}
    for token in parsed_tokens:
        token_parts = token.split('\t')
        word = token_parts[0]
        pos_info = token_parts[1].split(',')
        # Check if the word is a verb (動詞)
        if pos_info[0] == '動詞':
            verb_forms[word] = pos_info[6]  # pos_info[6] contains the verb form
    return verb_forms

# Example Japanese text
japanese_text = "彼は東京へ行った。そして、美味しい寿司を食べた。"

# Tokenize and parse the text
parsed_tokens = parse_japanese(japanese_text)

# Extract verb forms
verb_forms = extract_verb_forms(parsed_tokens)

# Output the verb forms alongside their corresponding words
for token in parsed_tokens:
    token_parts = token.split('\t')
    word = token_parts[0]
    if word in verb_forms:
        print(f"{word}: {verb_forms[word]}")
import MeCab
from collections import Counter
import re

# Tokenization function using MeCab
def tokenize_japanese(text):
    tagger = MeCab.Tagger("-Owakati")
    tokens = tagger.parse(text)
    return tokens.split()

# Function to filter out unwanted tokens
def filter_tokens(tokens):
    filtered_tokens = []
    for token in tokens:
        # Filter out punctuation marks and numbers
        if not re.match(r"^[!-@\[-`{-~、-〿ー-ヿ]*$", token):
            filtered_tokens.append(token)
    return filtered_tokens
# Function to extract verb forms
def extract_verb_forms(parsed_tokens):
    verb_forms = []
    for token in parsed_tokens:
        token_parts = token.split('\t')
        word = token_parts[0]
        pos_info = token_parts[1].split(',')
        # Check if the word is a verb (動詞)
        if pos_info[0] == '動詞':
            verb_forms.append((word, pos_info[6]))  # pos_info[6] contains the verb form
    return verb_forms

# Example Japanese text
japanese_text = "彼は東京へ行った。そして、美味しい寿司を食べた。"

# Tokenize the text
tokens = tokenize_japanese(japanese_text)
# Filter out unwanted tokens
filtered_tokens = filter_tokens(tokens)
# Extract verb forms
verb_forms = extract_verb_forms(filtered_tokens)

# Output the verb forms
for verb, form in verb_forms:
    print(f"{verb}: {form}")
# Example Japanese text
japanese_text = "ある日のこと、その男がふと立ち上がった。"



# Count the frequency of each token
word_freq = Counter(filtered_tokens)

# Output the vocabulary
vocabulary = list(word_freq.keys())
print(vocabulary)
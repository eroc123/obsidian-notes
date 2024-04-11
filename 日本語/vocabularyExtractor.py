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

# Example Japanese text
japanese_text = "ある日のこと、その男がふと立ち上がった。"

# Tokenize the text
tokens = tokenize_japanese(japanese_text)

# Filter out unwanted tokens
filtered_tokens = filter_tokens(tokens)

# Count the frequency of each token
word_freq = Counter(filtered_tokens)

# Output the vocabulary
vocabulary = list(word_freq.keys())
print(vocabulary)
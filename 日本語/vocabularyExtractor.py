from sudachipy import tokenizer
from sudachipy import dictionary

# Load Sudachi dictionary
sudachi = dictionary.Dictionary()

# Tokenize Japanese text
mode = tokenizer.Tokenizer.SplitMode.C
tokens = sudachi.tokenize("彼は東京へ行った。そして、美味しい寿司を食べた。", mode)

# Extract vocabulary
vocabulary = [token.surface() for token in tokens]
print(vocabulary)
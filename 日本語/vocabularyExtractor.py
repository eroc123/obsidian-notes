from sudachipy import tokenizer
from sudachipy import dictionary
# Tokenize Japanese text
mode = tokenizer.Tokenizer.SplitMode.B
# Load Sudachi dictionary
sudachi = dictionary.Dictionary().create(mode)


tokens = sudachi.tokenize("彼は東京へ行ったそして美味しい寿司を食べた。", mode)

# Extract vocabulary
vocabulary = [token.surface() for token in tokens]
print(vocabulary)
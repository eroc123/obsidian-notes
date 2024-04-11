from sudachipy import tokenizer
from sudachipy import dictionary
# Tokenize Japanese text
mode = tokenizer.Tokenizer.SplitMode.B
# Load Sudachi dictionary
sudachi = dictionary.Dictionary().create(mode)

userTextInp = input("input text to tokenize: ")
tokens = sudachi.tokenize(userTextInp, mode)

# Extract vocabulary
vocabulary = [token.surface() for token in tokens]
print(vocabulary)
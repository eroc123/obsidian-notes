from janome.tokenizer import Tokenizer

def extract_japanese_vocabulary(file_path):
    # Initialize Janome tokenizer
    tokenizer = Tokenizer()

    # Set to store unique words
    vocabulary = set()

    # Read the text file
    
    # Tokenize each line and extract words
    file = "台湾で3日、大きな地震が起こりました。5日の昼までに10人が亡くなって、1000人以上の人がけがをしました。大きな被害が出ています。台湾の人たちは、今まで日本で大きな地震などが起こると、寄付のお金をたくさん送ってくれました。2011年の東日本大震災のときは200億円以上、今年1月の能登半島地震のときは25億円以上の寄付をしてくれました。このため台湾の地震のあと、SNSには「台湾が助けてくれたことを忘れません」とか「今度は日本が台湾を助けましょう」などのことばが多くなっています。台湾と交流してきた市や町は、寄付のための箱を作ってお金を集めています。コンビニや日本赤十字社、NGOなども寄付を集めています。"
    
    tokens = tokenizer.tokenize(file)
    # Extract surface form (text) from each token
    words = [token.surface for token in tokens]
    # Add words to the vocabulary set
    vocabulary.update(words)

    return vocabulary

def main():
    file_path = input("Enter the path to the Japanese text file: ")
    vocabulary = extract_japanese_vocabulary(file_path)

    print("\nUnique Japanese vocabulary words in the text file:")
    for word in sorted(vocabulary):
        print(word)

if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup

def lookup_japanese_word(word):
    # URL of the online dictionary
    url = f"https://jisho.org/search/{word}"

    # Send HTTP GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the section containing the definitions
        definitions_section = soup.find('div', class_='meanings-wrapper')

        # Extract and print the definitions
        if definitions_section:
            print(f"Definitions for '{word}':")
            # Find all definition elements
            definitions = definitions_section.find_all('div', class_='meaning-meaning')
            for index, definition in enumerate(definitions, start=1):
                print(f"{index}. {definition.text.strip()}")
        else:
            print(f"No definitions found for '{word}'")
    else:
        print("Failed to fetch data from the dictionary.")

def main2():
    word = input("Enter the Japanese word you want to look up: ")
    lookup_japanese_word(word)

if __name__ == "__main__":
    main2()
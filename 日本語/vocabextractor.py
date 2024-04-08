import requests
from bs4 import BeautifulSoup

def extract_article_text(url, encoding='utf-8'):
    # Fetch the HTML content of the article
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    #find all paragraph tags
    paragraphs= soup.find_all('p')
    paragraph_text = []
    for paragraph in paragraphs:
        text = paragraph.get_text(strip=True)
        paragraph_text.append(text)
    return paragraph_text
# Example usage
url = "https://www3.nhk.or.jp/news/easy/k10014413031000/k10014413031000.html"
article_text = extract_article_text(url)
if article_text:
    print(article_text)
else:
    print("Failed to extract article text.")
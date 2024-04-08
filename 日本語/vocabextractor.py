import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    # Fetch the HTML content of the article
    response = requests.get(url, encoding = 'utf-8')
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main content of the article
    article_content = soup.find('article')

    # Extract text from the article content
    if article_content:
        article_text = article_content.get_text(separator='\n')
        return article_text
    else:
        return None

# Example usage
url = "https://www3.nhk.or.jp/news/easy/k10014413031000/k10014413031000.html"
article_text = extract_article_text(url)
if article_text:
    print(article_text)
else:
    print("Failed to extract article text.")
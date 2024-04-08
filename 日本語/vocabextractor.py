import requests
from selenium import webdriver
from bs4 import BeautifulSoup
#initalize webdriver
driver = webdriver.Chrome()
def extract_article_text(url, encoding='utf-8'):
    # Fetch the HTML content of the article
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    #find all paragraph tags
    paragraphs= soup.find_all('<main class="1-main easy-news">')
    title = soup.find_all('<h1 class="article_title">')
    paragraph_text = []
    for paragraph in paragraphs:
        text = paragraph.get_text(strip=True)
        paragraph_text.append(text)
    return paragraph_text
# Example usage
url = "https://www3.nhk.or.jp/news/easy/list/index.html?date=2024-04-07" #start off from april 7th week
article_text = extract_article_text(url)
if article_text:
    print(article_text)
else:
    print("Failed to extract article text.")
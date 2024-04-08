import requests
from bs4 import BeautifulSoup

def download_article_as_pdf(url, output_path):
    #fetch html content of article
    response = requests.get(url)
    html_content=response.text
    # Convert HTML content to PDF
    print(response.text)

# Example usage
url = "https://www3.nhk.or.jp/news/easy/k10014413031000/k10014413031000.html"
output_path = "article.pdf"

download_article_as_pdf(url, output_path)
import requests, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

#initalize webdriver
driver = webdriver.Chrome()
# Open the desired webpage
driver.get("https://www3.nhk.or.jp/news/easy/list/index.html?date=2024-04-07")
def navigateArticle(articleDate, currentDate):
    day = articleDate.
    link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dateStart")))
    print(link_element.text)
    weekDate = str(year) + "年" + str(month) + "月" + str(day) + "日"
    if weekDate.strip() in link_element.text.strip():
        print("this is the one")
    elif 



day = 8
month = 4
year = 2024
articleDate = datetime.datetime(year,month,day)
weekdayIndex = articleDate.weekday()
print(day-weekdayIndex)
#input both the date of the article to be found and the current date
navigateArticle(articleDate)
print(weekdayIndex)
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
import requests, datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

#initalize webdriver
driver = webdriver.Chrome()
# Open the desired webpage
driver.get("https://www3.nhk.or.jp/news/easy/list/index.html?date=2024-04-07")
def navigateArticle(articleDate):
    day = articleDate.day - articleDate.weekday() - 1
    month = articleDate.month
    year = articleDate.year
    #modify the date to be the date of the monday of the week - the date of the article to be found
    modifiedDate = datetime.datetime(year,month,day)
    while True:
        #get the week element and converts it to datetime format
        link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dateStart")))
        time.sleep(2)
        elementText = link_element.text.strip()
        print(elementText, "hello")
        for i in elementText:
            print(i)
        print(elementText[elementText.index("月")-1], "TEST")
        elementYear = elementText[0:4]
        print(elementYear, "year")
        elementMonth = elementText[(elementText.index("月") - 2):(elementText.index("月"))]
        print(elementMonth, "month")
        elementDay = elementText[elementText.index("日")-2:elementText.index("日")-1]
        print(elementYear, elementDay, elementMonth, "SADFADSFADSF")
        currentDate = datetime.datetime(int(elementYear), int(elementMonth), int(elementDay))
        print(currentDate)
        if currentDate == modifiedDate:
            print("this is the one")
            break
        elif modifiedDate < currentDate:
            previousElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "archives-pager__prev is-prev js-pager-nav")))
            previousElement.click()
        elif modifiedDate > currentDate:
            nextElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "archives-pager__next is-next js-pager-nav")))
            nextElement.click()
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
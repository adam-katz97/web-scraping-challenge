from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {'executable_path': '/Users/adamkatz/.wdm/drivers/chromedriver/mac64/87.0.4280.20/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()
    data={}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    data['news_title']=soup.find_all('div', class_='bottom_gradient')[0].text
    data['news_p']=soup.find_all('div', class_='article_teaser_body')[0].text


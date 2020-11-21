from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

def init_browser():
    executable_path = {'executable_path': '/Users/adamkatz/.wdm/drivers/chromedriver/mac64/87.0.4280.20/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html 
    soup = bs(html, 'lxml')
    news_title=soup.find_all('div', class_='bottom_gradient')[0].text
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text
    new_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(new_url)
    new_html = browser.html 
    new_soup = bs(new_html, 'lxml')
    featured_image_url=f"https://www.jpl.nasa.gov{new_soup.find('section', class_='main_feature').a['data-fancybox-href']}"
    fact_url='https://space-facts.com/mars/'
    fact_table=pd.read_html(fact_url)
    df=fact_table[0]
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
    ]

    data = {"news_title": news_title, "news_p":news_p, "featured_image_url": featured_image_url}
    browser.quit()
    return data
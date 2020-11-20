from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': '/Users/adamkatz/.wdm/drivers/chromedriver/mac64/87.0.4280.20/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()
    data={'news_title': news_title, 'news_p': news_p, 'featured_image_url': featured_image_url,
    'Mars facts': fact_table, 'Mars Pictues': hemisphere_image_urls}
    browser.quit()
    return data
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    info=mongo.db.collection.find_one()
    return render_template('index.html', mars=info)

@app.route("/scrape")
def scrape():
    data=scrape_mars.scrape()
    mongo.db.collection.update({}, data, upsert=True)
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
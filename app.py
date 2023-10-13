from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/visimisi')
def visimisi():
    return render_template('visimisi.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contactus')
def contactus():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')




if __name__=='__main__':
    app.run('0.0.0.0',port=5000, debug=True)
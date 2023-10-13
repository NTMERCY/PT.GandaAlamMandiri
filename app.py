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
    return render_template('templates/history.html')





if __name__=='__main__':
    app.run('0.0.0.0',port=5000, debug=True)
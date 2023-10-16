from flask import Flask, redirect, url_for, render_template, request, jsonify
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)

client=MongoClient('mongodb+srv://test:sparta@cluster0.qpc2myf.mongodb.net/?retryWrites=true&w=majority')
db=client.profil

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

@app.route('/contactus',methods=['GET'])
def contactus():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/editdata')
def editdata():
    return render_template('editdata.html')

@app.route('/tabel')
def tabel():
    return render_template('tabel.html')

@app.route('/pesan')
def pesan():
    return render_template('pesan.html')

@app.route('/tambahdata')
def tambahdata():
    return render_template('tambahdata.html')

@app.route('/contactus',methods=['POST'])
def tambah():
    name=request.form.get('name_give')
    email=request.form.get('email_give')
    message=request.form.get('message_give')
    print(name,email,message)

    doc={
        'name':name,
        'email':email,
        'message':message,
    }

    db.buah.insert_one(doc)
    return jsonify({
        'msg':'berhasil terkirim!'
    })

if __name__=='__main__':
    app.run('0.0.0.0',port=5000, debug=True)
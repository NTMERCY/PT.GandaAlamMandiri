from flask import Flask, redirect, url_for, render_template, request, jsonify, session
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)
app.secret_key = 'secretkey'

client=MongoClient('mongodb+srv://test:sparta@cluster0.qpc2myf.mongodb.net/?retryWrites=true&w=majority')
db=client.profil    

@app.route('/')
def home():
    data = list(db.pict.find({}).sort('_id',-1))
    return render_template('index.html',data=data)

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
    data = list(db.pict.find({}).sort('_id',-1))
    return render_template('gallery.html',data=data)

@app.route('/contactus',methods=['GET'])
def contactus():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        admin = db.admins.find_one({'username': username, 'password': password})

        if admin:
            session['admin_id'] = str(admin['_id'])
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)

    return render_template('login.html')

    
@app.route('/dashboard')
def admin_dashboard():
    if 'admin_id' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('admin_login'))
    
@app.route('/logout')
def admin_logout():
    session.pop('admin_id', None)
    return redirect(url_for('login.html'))

@app.route('/editdata')
def editdata():
    id =request.args.get('_id')
    data=list(db.pict.find({'_id' : ObjectId(id)}))
    return render_template('editdata.html', data=data)

@app.route('/editdata', methods=['POST'])
def editPost():
    id = request.form.get('id_give')
    file = request.files.get('file_give')
    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}.{extension}'
    save_to = f'static/{filename}'
    file.save(save_to)


    doc={
        'file': filename,
    }

    db.pict.update_one({'_id':ObjectId(id)}, {'$set':doc})
    return jsonify({ 'msg':'foto berhasil diubah' })


@app.route('/tabel',methods=['GET'])
def tabel():
    data = list(db.pict.find({}).sort('_id',-1))
    return render_template('tabel.html',data=data)

@app.route('/pesan')
def pesan():
    data=db.msg.find({})

    return render_template('pesan.html',data=data)

@app.route('/tambahdata')
def tambahdata():
    return render_template('tambahdata.html')

@app.route('/tambahdataPost', methods=['POST'])
def tambahdataPost():
    file = request.files.get('file_give')
    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}.{extension}'
    save_to = f'static/{filename}'
    file.save(save_to)


    doc={
        'file': filename,
    }

    db.pict.insert_one(doc)
    return jsonify({ 'msg':'berhasil terkirim!' })

@app.route('/contactusPost', methods=['POST'])
def tambah():
    name=request.form.get('name_give')
    email=request.form.get('email_give')
    message = request.form.get('message_give')


    doc={
        'name':name,
        'email':email,
        'message':message,
    }

    db.msg.insert_one(doc)
    return jsonify({ 'msg':'berhasil terkirim!' })

@app.route('/deletePhoto', methods=['GET'])
def delete_photo():
    #mengambil id dari sisi client
    id = request.args.get('_id')
    #menghapus foto berdasarkan foto yang dippilih dengan menggunakan id pada foto tersebut
    db.pict.delete_one({'_id':ObjectId(id)})
    data=list(db.pict.find({}))
    return render_template('tabel.html',data=data)

if __name__=='__main__':
    app.run('0.0.0.0',port=5000, debug=True)
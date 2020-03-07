from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os
# import werkzeug
import pymysql
import math
import datetime
import json
import os

with open('./templates/config.json', 'r') as file:
    params = json.load(file)["params"]

local_server = params["local_server"]

app = Flask(__name__)
app.secret_key = "DS"
app.config['Upload_File'] = params['upload_location']
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-username'],
    MAIL_PASSWORD=params['gmail-password']
)

mail = Mail(app)

if local_server == str("True"):
    app.config["SQLALCHEMY_DATABASE_URI"] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]

db = SQLAlchemy(app)


class Contact(db.Model):
    '''
    sno,name,email,message,phone_number,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String, nullable=True)


class Posts(db.Model):
    '''
    sno,title,tagline,content,slug,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True)


@app.route('/')
def home():
    all_posts = Posts.query.filter_by().all()
    # [0:params['no_of_posts']]
    last = math.ceil(len(all_posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = all_posts[(page-1)*params['no_of_posts']:(page-1) *
                      params['no_of_posts']+params['no_of_posts']]

    if page == 1:
        prev = '#'
        nextp = '/?page='+str(page+1)
    elif(page == last):
        prev = '/?page='+str(page-1)
        nextp = '#'
    else:
        prev = '/?page='+str(page-1)
        nextp = '/?page='+str(page+1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=nextp)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        #  ADD Entry to the Database
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        phone_number = request.form.get('phone_number')
        date = datetime.datetime.now()
        entry = Contact(name=name, email=email, date=date,
                        phone_number=phone_number, message=message)

        db.session.add(entry)
        db.session.commit()
        mail.send_message('New Message from Blog', sender=email, recipients=[params['gmail-username']],
                          body=message + '\n' + phone_number
                          )
    return render_template('contact.html', params=params)


@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if('user' in session and session['user'] == params['admin_user']):
        all_posts = Posts.query.filter_by().all()
        return render_template('dashboard.html', params=params, posts=all_posts)

    if request.method == 'POST':
        # Redirect to Admin Panel
        username = request.form.get('user')
        password = request.form.get('pass')
        if username == params['admin_user'] and password == params['admin_password']:
            # Set the Session variable
            session['user'] = username
            all_posts = Posts.query.filter_by().all()
            return render_template('dashboard.html', params=params, posts=all_posts)
    return render_template('login.html', params=params)


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
    if('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            '''
            title,tagline,slug,image,content
            '''
            title = request.form.get('title')
            subtitle = request.form.get('subtitle')
            slug = request.form.get('slug')
            img = request.form.get('img')
            content = request.form.get('content')

            if sno == '0' or sno == 0:
                post = Posts(title=title, subtitle=subtitle, content=content, slug=slug,
                             img_url=img, date=datetime.datetime.now())
                db.session.add(post)
                db.session.commit()
                return render_template('edit.html', params=params, sno=sno)

            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.slug = slug
                post.subtitle = subtitle
                post.img_url = img
                post.content = content
                post.date = datetime.datetime.now()

                db.session.add(post)
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            f = request.files['file']
            f.save(os.path.join(
                app.config['Upload_File'], f.filename))
            return "Uploaded Successfully !"


@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete(sno):
    if('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


app.run(debug=True)


from flask import render_template,request,redirect,url_for,session
from markupsafe import escape
from App import app,db
from App.Templates.Components.formLogin import LoginForm
from App.Templates.Components.formRegister import RegisterForm

import os,os.path
from App.Models.User import  User

from App.Controllers.loginController import AuthFinger,Register

# index routes
# @app.route("/", defaults = {"user": None})
# def index(user):
#     return render_template('index.html',user = user)

@app.route("/")
def index():
    if 'username' in session:
        return render_template('index.html',user = escape(session['username']))
    return redirect(url_for('login'))

# login route
@app.route("/login", methods =['POST','GET'])
def login():
    form = LoginForm()
    # validando formulário
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        
        userSelect = User.query.filter_by(username=form.username.data).first()
        # vaidando usuário
        if(userSelect!=None):

            # validando digital
            if AuthFinger(userSelect.fingerimage):
                session['username'] = form.username.data
                return redirect(url_for('index'), code=302)
                
            errorFinger = "Digital não cadastrada ou incorreta"
            return render_template('login.html', form = form,errorBd = errorFinger)

        # print(form.errors)
        errorUser = 'Usuário nao encontrado'
        return render_template('login.html', form = form,errorBd = errorUser)

    print(form.errors)
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

# register route
@app.route("/register", methods =['POST','GET'])
def register():
    form = RegisterForm()
    userExist = User.query.filter_by(username=form.username.data).first()

    if userExist:
        return render_template('register.html', form = form,messageBd = "Nome de usuário já em uso, escolha outro!" , user = escape(session['username']))

    if form.validate_on_submit():
        fingerImageName = Register()
        createUser = User(form.username.data, form.password.data, form.name.data, fingerImageName, form.email.data, form.nivel.data)
        db.session.add(createUser)
        db.session.commit()
        form= RegisterForm()
        return render_template('register.html', form = form, messageBd="Cadastrado com sucesso" ,user = escape(session['username']))

    return render_template('register.html', form = form, user = escape(session['username']))




@app.route("/create")
def create():
    i = User("jonathasa","123","jonathas augusto", "/Images/a.png", "a@gmail.com",1)
    db.session.add(i)
    db.session.commit()
    return "CREATE"

@app.route("/select")
def select():
    r = User.query.filter_by(username="jonathasa").first()
    print(r.username)
    return "READ"

@app.route("/update")
def update():
    u = User.query.filter_by(username="jonathas").first()
    u.username="jonathasUPDATE"
    print(u.username)
    db.session.add(u)
    db.session.commit()
    return "UPDATEE"

@app.route("/delete")
def delete():
    d = User.query.filter_by(username="jonathasUPDATE").first()
    db.session.delete(d)
    db.session.commit()
    return "DELETADO"

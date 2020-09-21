
from flask import render_template,request
from App import app,db
from App.Templates.Components.formLogin import LoginForm

from App.Models.User import  User

from App.Controllers.loginController import AuthFinger

# index routes
@app.route("/index/<user>")
@app.route("/", defaults = {"user": None})
def index(user):
    return render_template('index.html',user = user)

# login route
@app.route("/login", methods =['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():       
        print(form.username.data)
        print(form.password.data)
        AuthFinger()

        return render_template('index.html')
    else:
        print(form.errors)
        return render_template('login.html', form = form)

# register route
@app.route("/register")
def register():
    return render_template('register.html', user = [1, 2, 3, 4])

@app.route("/create")
def create():
    i = User("jonathasa","123","jonathas", "/Imagem/a.png")
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

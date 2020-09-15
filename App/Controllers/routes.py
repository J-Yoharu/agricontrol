
from flask import render_template
from App import app
from App.Templates.Components.formLogin import LoginForm

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
    else:
        print(form.errors)
    return render_template('login.html', form = form)

# register route
@app.route("/register")
def register():
    return render_template('register.html', user = [1, 2, 3, 4])



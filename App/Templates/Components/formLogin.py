from flask_wtf import Form
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("Senha", validators = [DataRequired()])
    image = FileField("imagem", validators = [DataRequired()])
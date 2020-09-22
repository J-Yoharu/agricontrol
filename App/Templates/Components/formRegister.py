from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SelectField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("Senha")
    image = FileField("image", validators = [DataRequired()])
    email = StringField("email",validators = [DataRequired()])
    nivel = SelectField("Nível de acesso", choices=["1","2","3"])

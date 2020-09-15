from App import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    fingerimage = db.Column(db.String)

    def __init__(self, username, password, name, fingerimage):
        self.username = username
        self.password = password
        self.name = name
        self.fingerimage = fingerimage

    def __repr(self):
        return "<User %r>" % self.username
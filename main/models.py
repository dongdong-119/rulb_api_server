from main import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color
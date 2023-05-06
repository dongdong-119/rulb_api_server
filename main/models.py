from main import db


class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_to = db.Column(db.String, nullable=False)
    email_from = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text(), nullable=True)

    def __init__(self, email_to, email_from, name, title, content):
        self.email_to = email_to
        self.email_from = email_from
        self.name = name
        self.title = title
        self.content = content
from ButtShortener import db


class ShortURL(db.Model):
    key = db.Column(db.String(32), primary_key=True)
    target = db.Column(db.Text)
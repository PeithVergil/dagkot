from google.appengine.ext import db

class Dagkot(db.Model):
    type = db.StringProperty()
    candle = db.StringProperty()
    author = db.StringProperty()
    message = db.StringProperty(multiline=True)
    receiver = db.StringProperty()
    postdate = db.DateTimeProperty(auto_now_add=True)
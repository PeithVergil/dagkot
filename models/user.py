from google.appengine.ext import db

class UserProfile(db.Model):
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    birthdate = db.StringProperty()
    userid = db.StringProperty()
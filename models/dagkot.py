from google.appengine.ext import db

# class User(db.Model):
# 	user_key = db.StringProperty()
# 	user_name = db.StringProperty()
# 	user_email = db.StringProperty()

class Candle(db.Model):
	candle_type = db.StringProperty()
	candle_path = db.StringProperty()
	candle_name = db.StringProperty()

class Dagkot(db.Model):
    dagkot_for = db.StringProperty()
    dagkot_type = db.StringProperty()
    dagkot_date = db.DateTimeProperty(auto_now_add=True)
    dagkot_author = db.UserProperty(auto_current_user_add=True)
    dagkot_candle = db.ReferenceProperty(Candle)
    dagkot_message = db.StringProperty(multiline=True)
    dagkot_pictures = db.StringListProperty()

    # def get_pictures(self):
    #     photos = Photo.all().filter('photo_dagkot =', self.key())

    #     keys = []
    #     for photo in photos:
    #         photo_k = db.Key.from_path('Photo', photo.photo_key)
    #         keys.append(photo_k)

    #     return db.get(keys)

class Photo(db.Model):
    photo_key = db.StringProperty()
    photo_path = db.StringProperty()
    photo_dagkot = db.ReferenceProperty(Dagkot)
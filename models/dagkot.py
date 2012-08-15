from google.appengine.api import images
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

    def get_pictures(self):
        count = 0
        for picture in self.dagkot_pictures:
            count += 1

            if count == 1:
                yield images.get_serving_url(picture, 205)
            else:
                yield images.get_serving_url(picture, 48, True)

class Photo(db.Model):
    photo_key = db.StringProperty()
    photo_path = db.StringProperty()
    photo_dagkot = db.ReferenceProperty(Dagkot)
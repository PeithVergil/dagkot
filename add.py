from google.appengine.api import users

import webapp2

import base

from models.dagkot import Candle, Dagkot
        
class Add(base.BaseRequestHandler):
    def get(self):
        data = {
            'dagkot_for': self.request.get('txt_dagkot_for')
        }
        
        self.render_html('home/add.html', **data)
        
    def post(self):
        dagkot_for = self.request.get('dagkot_for')
        dagkot_msg = self.request.get('dagkot_msg')
        dagkot_type = self.request.get('dagkot_type')

        dagkot_candle_type = self.request.get('dagkot_candle_type')
        dagkot_candle_path = self.request.get('dagkot_candle_path')
        dagkot_candle_name = self.request.get('dagkot_candle_name')

        candle = Candle(candle_type=dagkot_candle_type, candle_path=dagkot_candle_path,
            candle_name=dagkot_candle_name)

        candle_key = candle.put()
        if candle_key:
            user = users.get_current_user()
            
            dagkot = Dagkot(dagkot_author=user, dagkot_for=dagkot_for, dagkot_message=dagkot_msg,
                dagkot_type=dagkot_type, dagkot_candle=candle)
        
            dagkot_key = dagkot.put()
            if dagkot_key:
                self.redirect('/upload/images/%s' % dagkot_key)
            else:
                self.redirect('/add/error')
        else:
            self.redirect('/add/error')

class AddError(base.BaseRequestHandler):
    def get(self):
        data = {
            'message_type'   : 'ERROR',
            'message_content': 'There was an error in saving your dagkot. Please try again.'
        }
        self.render_html('home/landing.html', **data)
        
app = base.create_wsgi_app([
    ('/add', Add), ('/add/error', AddError)
], debug=True)
from google.appengine.api import users

import webapp2

import base

from models.dagkot import Dagkot
        
class Home(base.BaseRequestHandler):
    def get(self):
        data = {}
        
        user = users.get_current_user()
        if user:
            data['dagkots'] = Dagkot.all().filter('author =', user.user_id()).order('-postdate')
        else:
            data['dagkots'] = Dagkot.all().order('-postdate')
        
        self.render_html('home/get.html', **data)
        
    def post(self): 
        data = {
            'message': self.request.get('greeting')
        }
        
        self.render_html('home/post.html', **data)
        
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
        dagkot_candle = self.request.get('dagkot_candle')
        
        user = users.get_current_user()
        
        dagkot = Dagkot(author=user.user_id(), receiver=dagkot_for,
            message=dagkot_msg, type=dagkot_type, candle=dagkot_candle)
        
        key = dagkot.put()
        if key:
            self.redirect('/')
        

app = webapp2.WSGIApplication([
    ('/', Home), ('/add', Add)
], debug=True)
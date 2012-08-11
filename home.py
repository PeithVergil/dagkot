from google.appengine.api import users

import webapp2

import base

from models.dagkot import Dagkot
        
class Home(base.BaseRequestHandler):
    def get(self):
        data = {}
        
        user = users.get_current_user()
        if user:
            data['dagkots'] = Dagkot.all().filter('dagkot_author =', user).order('-dagkot_date')
        else:
            data['dagkots'] = Dagkot.all().order('-dagkot_date')
        
        self.render_html('home/home.html', **data)
        
app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)
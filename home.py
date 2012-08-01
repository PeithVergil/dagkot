from google.appengine.api import users

import webapp2

import base
        
class Home(base.BaseRequestHandler):
    def get(self):
        data = {}
        
        if not users.get_current_user():
            data['link_url'] = users.create_login_url(self.request.uri)
            data['link_txt'] = 'Login'
        else:
            data['link_url'] = users.create_logout_url(self.request.uri)
            data['link_txt'] = 'Logout'
        
        self.render_html('home/get.html', **data)
        
    def post(self): 
        data = {
            'message': self.request.get('greeting')
        }
        
        self.render_html('home/post.html', **data)
        

app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)
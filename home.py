import os

from google.appengine.api import users

import jinja2
import webapp2

templates = os.path.join(os.path.dirname(__file__), 'templates')

jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates)
)
        
class Home(webapp2.RequestHandler):
    def get(self):
        data = {}
        
        if not users.get_current_user():
            data['link_url'] = users.create_login_url(self.request.uri)
            data['link_txt'] = 'Login'
        else:
            data['link_url'] = users.create_logout_url(self.request.uri)
            data['link_txt'] = 'Logout'
        
        tpl = jinja.get_template('hello_hello.html')
        self.response.out.write(tpl.render(data))
        
    def post(self):
        tpl = jinja.get_template('hello_hello.html')
        
        data = {
            'message': self.request.get('greeting')
        }
        
        self.response.out.write(tpl.render(data))
        

app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)
from google.appengine.api import users

from webapp2 import cached_property
from webapp2 import RequestHandler
from webapp2_extras import jinja2

class BaseRequestHandler(RequestHandler):
    '''
    The base class for all request handlers.
    '''
    
    @cached_property
    def jinja(self):
        return jinja2.get_jinja2(app=self.app)
        
    def render_html(self, template, **params):
        user = users.get_current_user()
        if user:
            params['auth_url'] = users.create_logout_url('/')
            params['auth_txt'] = 'Logout'
            
            params['nickname'] = user.nickname()
        else:
            params['auth_url'] = users.create_login_url('/')
            params['auth_txt'] = 'Login'
        params['user'] = user
        
        tpl = self.jinja.render_template(template, **params)
        
        self.response.write(tpl)
        
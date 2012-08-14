import json

from google.appengine.api import users

from webapp2 import cached_property
from webapp2 import RequestHandler
from webapp2_extras import jinja2

class BaseRequestHandler(RequestHandler):
    '''
    The base class for all request handlers.
    '''
    
    def get_context(self):
        context = {}
        
        user = users.get_current_user()
        if user:
            context['auth_url'] = users.create_logout_url('/')
            context['nickname'] = user.nickname()
            context['auth_txt'] = 'Logout'
        else:
            context['auth_url'] = users.create_login_url('/')
            context['auth_txt'] = 'Login'
        context['user'] = user
        
        return context
    
    @cached_property
    def jinja(self):
        return jinja2.get_jinja2(app=self.app)
        
    def render_html(self, template, **params):
        context = self.get_context()
        
        for key, val in params.items():
            context[key] = val
        
        tpl = self.jinja.render_template(template, **context)
        
        self.response.write(tpl)

    def render_json(self, data):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))
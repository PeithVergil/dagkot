import json

from google.appengine.api import users

from webapp2 import cached_property
from webapp2 import RequestHandler
from webapp2 import WSGIApplication
from webapp2_extras import jinja2
from webapp2_extras import sessions

class BaseRequestHandler(RequestHandler):
    '''
    The base class for all request handlers.
    '''

    def dispatch(self):
        self.session_store = sessions.get_store(factory=sessions.SessionStore, key='webapp2_extras.sessions.SessionStore', request=self.request)
        self.session_flash = sessions.get_store(factory=sessions.SessionDict, key='webapp2_extras.sessions.SessionDict', request=self.request)

        try:
            RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)
    
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

    @cached_property
    def session(self):
        return self.session_store.get_session()

    @cached_property
    def flash(self):
        return self.session_flash
        
    def render_html(self, template, **params):
        context = self.get_context()
        
        for key, val in params.items():
            context[key] = val
        
        tpl = self.jinja.render_template(template, **context)
        
        self.response.write(tpl)

    def render_json(self, data):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))

def create_wsgi_app(routes, debug=False, config={}):
    config['webapp2_extras.sessions'] = {
        'secret_key': 'ru#qgro%ta=lc*wohb%)rqg*^)x6hn=tr)2@&amp;4d^&amp;j%i$sae)@'
    }
    return WSGIApplication(routes, debug=debug, config=config)
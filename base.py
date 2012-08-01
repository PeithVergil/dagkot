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
        tpl = self.jinja.render_template(template, **params)
        self.response.write(tpl)
        
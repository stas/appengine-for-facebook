import os

from google.appengine.ext.webapp import template, RequestHandler

from utils.facebook.webappfb import FacebookRequestHandler
from utils.config import Config

class HomePage(FacebookRequestHandler):
    def reinit(self):
        c = Config('facebook')
        
        #if not self.facebook.uid:
        #    self.redirect( self.facebook.get_app_url() )
        
        self.args = dict(
            app_key = c.id('api_key'),
            app_url = 'http://apps.facebook.com/' + c.id('app_name') + '/',
        )
    
    def post(self):
        self.get()
    
    def get(self):
        args = None
        self.reinit()
        if hasattr(self, 'args'):
            args = self.args
        
        path = os.path.join(os.path.dirname(__file__), 'views/home.fbml')
        self.response.out.write(template.render(path, args))
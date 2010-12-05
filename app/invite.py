import os
import string
import logging

from google.appengine.ext.webapp import template

from utils.facebook.webappfb import FacebookRequestHandler
from utils.user import User
from utils.config import Config

class InvitePage(FacebookRequestHandler):
    requires_login = True
    
    def reinit(self):
        c = Config('facebook')
        FACEBOOK_CONFIG = c.data
        
        self.initialize(self.request, self.response)
        
        self.facebook.in_canvas = True
        
        self.args = dict(
            uid = self.facebook.uid,
            app_key = self.facebook.api_key,
            app_url = self.facebook.get_app_url(),
            granted = True,
        )

    def get(self):
        self.reinit()
        args = self.args
        
        path = os.path.join(os.path.dirname(__file__), 'views/invite.fbml')
        self.response.out.write(template.render(path, args))

    def post(self):
        self.get()
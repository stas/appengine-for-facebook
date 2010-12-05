from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from app.home import HomePage
from app.invite import InvitePage

application = webapp.WSGIApplication(
    [
        ('/', HomePage),
        ('/invite', InvitePage),
    ],
    debug=False)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

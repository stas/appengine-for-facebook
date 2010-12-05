from google.appengine.ext import db
from google.appengine.ext import search

class User(search.SearchableModel, db.Model):
    uid = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    email = db.EmailProperty()
    birthday_date = db.DateProperty()
    network = db.StringProperty()
    website = db.LinkProperty()
    pic_square = db.LinkProperty()
    cell_number = db.PhoneNumberProperty()
    current_location = db.StringProperty()
    relationship_status = db.StringProperty()
    sex = db.StringProperty()
    INDEX_ONLY = ['name', 'current_location']

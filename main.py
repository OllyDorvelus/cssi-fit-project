
import os
import jinja2
import webapp2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Event(ndb.Model):
    db_firstname = ndb.StringProperty(required=True)
    db_lastname = ndb.StringProperty(required=True)
    db_eventname = ndb.StringProperty(required=True)
    db_description = ndb.StringProperty(required=True)
    db_start_time = ndb.StringProperty(required=True)
    db_end_time = ndb.StringProperty(required=True)
    db_image = ndb.BlobProperty()

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('')
        self.response.write(template.render())
class EventMaker(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('make_event.html')
        self.response.write(template.render())
    # def post(self):
    #     redirect
# class OneEvent(webapp2.RequestHandler):
#     def get(self):


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/eventmaker', EventMaker)
], debug=True)


import os
import jinja2
import webapp2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MakeEvent(ndb.Model):
    db_firstname = ndb.StringProperty(required=True)
    db_lastname = ndb.StringProperty(required=True)
    db_eventname = ndb.StringProperty(required=True)
    db_description = ndb.StringProperty(required=True)
    db_image = ndb.BlobProperty()

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render())
class AboutPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class EventMaker(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('make_event.html')
        self.response.write(template.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        event_query = MakeEvent.query()
        events = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render({'events': events}))



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/eventmaker', EventMaker),
    ('/results', ResultsPage),
    ('/about', AboutPage)
], debug=True)

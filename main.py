
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
    db_location = ndb.StringProperty(required=True)
    db_description = ndb.StringProperty(required=True)
    db_start_time = ndb.StringProperty(required=True)
    db_end_time = ndb.StringProperty(required=True)
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
#<<<<<<< HEAD
#=======
    def post(self):
        first_name = self.request.get('firstname')
        last_name = self.request.get('lastname')
        eventname = self.request.get('event_name')
        location = self.request.get('location')
        starttime = self.request.get('start_time')
        endtime = self.request.get('end_time')
        description = self.request.get('descrip')
        image = self.request.get('filename')
        event_entry = Event(db_firstname=first_name, db_lastname=last_name, db_eventname=eventname, db_location=location,
         db_description=description, db_start_time=starttime, db_end_time=endtime, db_image=image)
        key = event_entry.put()
        template_values={
        'eventname': eventname,
        'firstname': first_name,
        'lastname': last_name,
        'location': location,
        'starttime': starttime,
        'endtime': endtime,
        'description':description}
        template = JINJA_ENVIRONMENT.get_template('view_event.html')
        self.response.write(template.render(template_values))
class ViewEvent(webapp2.RequestHandler):
    def get(self):
        event_query = Event.query()
        myevents = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('view_event.html')
        self.response.write(template.render({"events":myevents}))

#>>>>>>> a0fd4b28b24391760174af9e07f544b1a81aec9a

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        event_query = Event.query()
        event = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('results.html')
#<<<<<<< HEAD
        self.response.write(template.render({'events': event}))
#=======
        self.response.write(template.render())
#>>>>>>> 552c95d91b0d1490f0589ce2d5caa28d4d5d0387
#>>>>>>> a0fd4b28b24391760174af9e07f544b1a81aec9a



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/eventmaker', EventMaker),
    ('/results', ResultsPage),
#<<<<<<< HEAD
    ('/viewevent', ViewEvent),
#=======
    ('/about', AboutPage)
#>>>>>>> 584609c3f4c99bbdf913e676398c7e2e3c8c79d6
], debug=True)

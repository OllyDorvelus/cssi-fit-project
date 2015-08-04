
import os
import jinja2
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

# from google.appengine.ext import blobstore
# from google.appengine.ext.webapp import blobstore_handlers
# from google.appengine.ext.webapp.util import run_wsgi_app


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
    db_date = ndb.StringProperty(required=True)
    db_image = ndb.BlobProperty(required=False)

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render())
    def post(self):
        res_query = Event.query()
        results = res_query.fetch()
        self.redirect("/results")
class AboutPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class EventMaker(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('make_event.html')
        self.response.write(template.render())
    def post(self):
        first_name = self.request.get('firstname')
        last_name = self.request.get('lastname')
        eventname = self.request.get('event_name')
        location = self.request.get('location')
        starttime = self.request.get('start_time')
        endtime = self.request.get('end_time')
        description = self.request.get('descrip')
        date = self.request.get('date_time')
        image = str(self.request.get('img'))
        event_entry = Event(db_firstname=first_name, db_lastname=last_name, db_eventname=eventname, db_location=location,
         db_description=description, db_start_time=starttime, db_end_time=endtime, db_date=date, db_image=image)
        event_entry.put()
        # template = JINJA_ENVIRONMENT.get_template('view_event.html')
        # self.response.write(template.render())
        self.redirect('/viewevent')
class ViewEvent(webapp2.RequestHandler):
    def get(self):
        event_query = Event.query()
        myevents = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('view_event.html')
        self.response.write(template.render({"events":myevents}))


class ResultsPage(webapp2.RequestHandler):
    def get(self):
        event_query = Event.query()
        event = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render({'events': event}))
    def get(post):
        # All of the terms in the search query.

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write("<html><body>%s</body></html>" % greeting)


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/eventmaker', EventMaker),
    ('/results', ResultsPage),



    ('/viewevent', ViewEvent),

    ('/about', AboutPage),


    ('/viewevent', ViewEvent),

    ('/about', AboutPage),


    ('/viewevent', ViewEvent),
    ('/about', AboutPage),
    ('/login', LoginHandler)

], debug=True)

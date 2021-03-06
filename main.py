import os
import jinja2
import webapp2
# import sys
#
# import sys
#
# reload(sys)
# sys.setdefaultencoding('byte_string')
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import urllib
import json

# from google.appengine.ext import blobstore
# from google.appengine.ext.webapp import blobstore_handlers
# from google.appengine.ext.webapp.util import run_wsgi_app
# upload_url = blobstore.create_upload_url('/img')
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
        search_term = self.request.get("search")
        #search eventbrite API
        url = "https://www.eventbriteapi.com/v3/events/search?categories=107,108&venue.region=NY&q="
        api_key = "&token=QFYVYGNAS5ENNEEHHXLI"
        event_data_source = urlfetch.fetch(url + search_term +  api_key )
        event_json_content = event_data_source.content
        display = json.loads(event_json_content)
        parsed_event_dictionary = json.loads(event_json_content)
        template = JINJA_ENVIRONMENT.get_template('results.html')
        #search our database
        event_query = Event.query()
        event_data = event_query.fetch()
        event_list = []
        for eventobj in event_data:
            if search_term in eventobj.db_eventname or search_term in eventobj.db_description:
                event_list.append(eventobj)
        #results page
        dictionary = {'events':parsed_event_dictionary['events'][:30],
                       'moreevents':event_list}
        self.response.write(template.render(dictionary))

class PracticeHandler(webapp2.RequestHandler):
    def get(self):
        event_id = int(self.request.get('id'))
        self.response.write(event_id)

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
        starttime = str(self.request.get('start_time'))
        endtime = str(self.request.get('end_time'))
        description = self.request.get('descrip')
        date = str(self.request.get('date_time'))
        image = self.request.get('img')
        event_entry = Event(db_firstname=first_name, db_lastname=last_name, db_eventname=eventname, db_location=location,
         db_description=description, db_start_time=starttime, db_end_time=endtime, db_date=date, db_image=image)
        key=event_entry.put()
        # template = JINJA_ENVIRONMENT.get_template('view_event.html')
        # self.response.write(template.render())
        self.redirect('/view_event?id='+str(key.id()))

class ViewEvent(webapp2.RequestHandler):
    def get(self):
        event_id=int(self.request.get('id'))
        event=Event.get_by_id(event_id)
        # event_query = Event.query()
        # myevents = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('view_event.html')
        self.response.write(template.render({'event':event}))

class ViewApiEvent(webapp2.RequestHandler):
    def get(self):
        event_id=int(self.request.get('id'))
        # venue_id= int(self.request.get('v'))
        url = 'https://www.eventbriteapi.com/v3/events/'
        api_key = "?token=QFYVYGNAS5ENNEEHHXLI"
        event=urlfetch.fetch(url+str(event_id)+api_key)
        event = json.loads(event.content)

        # urlv = 'https://www.eventbriteapi.com/v3/venues/'
        # venue=urlfetch.fetch(urlv+str(venue_id)+api_key)
        # venue=json.loads(venue.content)
        template = JINJA_ENVIRONMENT.get_template('viewapievent.html')
        self.response.write(template.render({'event':event}))

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        event_query = Event.query()
        event = event_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render({'events': event}))
class FitTips(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('fun.html')
        self.response.write(template.render())
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
        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render())

# [START image_handler]
class Image(webapp2.RequestHandler):
    def get(self):
        event_key = ndb.Key(urlsafe=self.request.get('event_url_key'))
        event = event_key.get()
        if event.db_image:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(event.db_image)
        else:
            self.response.out.write('No image')
# [END image_handler]

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/img', Image),
    ('/eventmaker', EventMaker),
    ('/results', ResultsPage),
    ('/view_event', ViewEvent),
    ('/viewapievent', ViewApiEvent),
    ('/about', AboutPage),
    ('/login', LoginHandler),
    ('/practice', PracticeHandler),
    ('/fittips', FitTips)
], debug=True)

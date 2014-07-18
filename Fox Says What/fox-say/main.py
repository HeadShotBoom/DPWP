
import webapp2
from animals import *


class MainHandler(webapp2.RequestHandler):
    def get(self):





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

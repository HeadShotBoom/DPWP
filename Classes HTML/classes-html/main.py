
import webapp2
from pages import Page  # From package "pages.py" import the Page class


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

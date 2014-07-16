
import webapp2
from pages import Page  # From package "pages.py" import the Page class


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My Page"
        p.body = "Miss Piggy likes Kermit De Frog!"
        self.response.write(p.whole_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


import webapp2
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "Encapsulated Calculator"
        p.css = "css/styles.css"
        p.body = "<h1>It Works</h1>"
        self.response.write(p.whole_page)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

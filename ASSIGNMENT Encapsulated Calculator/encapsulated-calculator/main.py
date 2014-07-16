
import webapp2
from pages import Page
from cameras import Cameras


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "Encapsulated Calculator"
        p.css = "css/styles.css"
        p.camera = self.request.GET["cameras"]
        print p.camera
        self.response.write(p.whole_page)

        c1 = Cameras()
        c1.body_cost = 1000
        c1.lens_cost = 500
        c1.accessories_cost = 100
        c1.quality = "High"

        c2 = Cameras()
        c2.body_cost = 500
        c2.lens_cost = 1500
        c2.accessories_cost = 100
        c2.quality = "Low"

        c3 = Cameras()
        c3.body_cost = 100
        c3.lens_cost = 500
        c3.accessories_cost = 100
        c3.quality = "Medium"

        c4 = Cameras()
        c4.body_cost = 2000
        c4.lens_cost = 5000
        c4.accessories_cost = 100
        c4.quality = "High"

        c5 = Cameras()
        c5.body_cost = 10000
        c5.lens_cost = 5000
        c5.accessories_cost = 1100
        c5.quality = "Low"



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

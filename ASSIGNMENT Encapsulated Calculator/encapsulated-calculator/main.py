
import webapp2
from pages import Page
from cameras import Cameras


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "Encapsulated Calculator"
        p.css = "css/styles.css"

        c1 = Cameras()
        c1.name = "Canon 5d3"
        c1.body_cost = 3000
        c1.lens_cost = 5000
        c1.accessories_cost = 1000
        c1.quality = "High"
        c1.calc_value()

        c2 = Cameras()
        c2.name = "Nikon D800"
        c2.body_cost = 2500
        c2.lens_cost = 1500
        c2.accessories_cost = 200
        c2.quality = "Low"
        c2.calc_value()

        c3 = Cameras()
        c3.name = "Leica M9"
        c3.body_cost = 100
        c3.lens_cost = 500
        c3.accessories_cost = 100
        c3.quality = "Medium"
        c3.calc_value()

        c4 = Cameras()
        c4.name = "Pentax MX1"
        c4.body_cost = 2000
        c4.lens_cost = 200
        c4.accessories_cost = 50
        c4.quality = "High"
        c4.calc_value()

        c5 = Cameras()
        c5.name = "GoPro Hero5 Platinum"
        c5.body_cost = 10000
        c5.lens_cost = 0
        c5.accessories_cost = 10
        c5.quality = "Low"
        c5.calc_value()

        all_these_cameras = [c1, c2, c3, c4, c5]



        if "cameras" in self.request.GET:
            p.current_camera = all_these_cameras[int(self.request.GET["cameras"])]
            self.response.write(p.whole_page)
        else:
            self.response.write(p.whole_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

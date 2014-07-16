
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
        c1.body_cost = 1000
        c1.lens_cost = 500
        c1.accessories_cost = 100
        c1.quality = "High"

        c2 = Cameras()
        c2.name = "Nikon D800"
        c2.body_cost = 500
        c2.lens_cost = 1500
        c2.accessories_cost = 100
        c2.quality = "Low"

        c3 = Cameras()
        c3.name = "Leica M9"
        c3.body_cost = 100
        c3.lens_cost = 500
        c3.accessories_cost = 100
        c3.quality = "Medium"

        c4 = Cameras()
        c4.name = "Pentax P&S"
        c4.body_cost = 2000
        c4.lens_cost = 5000
        c4.accessories_cost = 100
        c4.quality = "High"

        c5 = Cameras()
        c5.name = "GoPro Hero5 Platinum"
        c5.body_cost = 10000
        c5.lens_cost = 5000
        c5.accessories_cost = 1100
        c5.quality = "Low"

        all_these_cameras = [c1, c2, c3, c4, c5]

        if "cameras" in self.request.GET:
            p.camera = self.request.GET["cameras"]
            if p.camera == "c1":
                this_camera = 0
            elif p.camera == "c2":
                this_camera = 1
            elif p.camera == "c3":
                this_camera = 2
            elif p.camera == "c4":
                this_camera = 3
            elif p.camera == "c5":
                this_camera = 4
            else:
                pass
            p.display = all_these_cameras[this_camera].value
            print p.display
            self.response.write(p.whole_page)
        else:
            self.response.write(p.whole_page)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

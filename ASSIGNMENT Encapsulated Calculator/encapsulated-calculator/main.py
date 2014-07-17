# The following lines control what elements get imported into the page
import webapp2
# This imports the Page class from the pages.py file The following line does something similar.
from pages import Page
from cameras import Cameras

# This is my main class that interacts with the browser and receives requests.
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Establishes p as referring to the Page class
        p = Page()
        # p.title uses the title setter in the Page class to set the value of title, the line below is similar
        p.title = "Encapsulated Calculator"
        p.css = "css/styles.css"

        # c1 uses the Cameras class to assemble an object with the following attributes and sets their values
        # c2=c5 is identical in function
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

        # This establishes a variable that consolisates all c1-c5 objects
        all_these_cameras = [c1, c2, c3, c4, c5]


        # Checks if there is an instance of "cameras" in the request pushed from the browser
        if "cameras" in self.request.GET:
            # Uses a value in the request to determine which cX object I am requesting
            # and sets just that object to the current_camera variable in Page class.
            p.current_camera = all_these_cameras[int(self.request.GET["cameras"])]
            # Writes the entire contents of whole_page variable in Page class to the browser
            self.response.write(p.whole_page)
        else:
            # Writes the info to the browser even if a request hasnt been made.
            self.response.write(p.whole_page)


# This is Magic, don't touch this or Rebbecca will be MAD!!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

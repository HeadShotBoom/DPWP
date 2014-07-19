
import webapp2
# This imports all classes from animals.py and Page class from pages.py
from animals import *
from pages import Page

# Main handler of the app. Interacts with the browser
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Establishes variables to allow interaction with designated class.
        a1 = Snake()
        a2 = Bird()
        a3 = Person()
        # Stores all animals defined in object
        self.animals = [a1, a2, a3]
        # Defines p as referring to Page class
        p = Page()
        # Runs the update command on page to concatinate the first pages info
        p.update()

        # Listens for an occurance of animal in the browsers request. Essentially listening for a button click
        if "animal" in self.request.GET:
            # Sets current animals value based on which request was made
            p.current_animal = self.animals[int(self.request.GET["animal"])]
            # Changes the Title of the page to match the selected animal
            p.title = self.animals[int(self.request.GET["animal"])].name
            # plays the sound specific for that animal
            p.loud_noises = self.animals[int(self.request.GET["animal"])].sound
            # Writes contents of whole page to the browser. The update function assembles this
            self.response.write(p.whole_page)
        else:
            self.response.write(p.whole_page)




# Here be dragons
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


import webapp2
from animals import *
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):

        a1 = Snake()
        a2 = Bird()
        a3 = Person()
        a = Animal()
        self.animals = [a1, a2, a3]

        p = Page()
        p.loud_noises = a.sound


        p.update()
        if "animal" in self.request.GET:
            p.current_animal = self.animals[int(self.request.GET["animal"])]
            p.title = self.animals[int(self.request.GET["animal"])].name
            p.loud_noises = self.animals[int(self.request.GET["animal"])].sound
            self.response.write(p.whole_page)
        else:
            self.response.write(p.whole_page)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

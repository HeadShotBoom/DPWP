"""
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Final Project
"""


import webapp2
import urllib2 # python classes and code needed to open up url info
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() # This needs to refer to the submost class you are wanting to use


        if self.request.GET:
            #get info from the API
            movie = self.request.GET['movie']
            new_movie = movie.replace(" ","+")
            url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=zt3u3utgzsba8qdy3bwcaf6g&q=" + new_movie + "&page_limit=1"
            #Assemble the request
            request = urllib2.Request(url)
            #Use URLLIB2 Library to create object to get url
            opener = urllib2.build_opener()
            #Use URL to get result - request info from API
            result = opener.open(request)

            #parsoing the json
            jsondoc = json.load(result)

            self.name = jsondoc['movies'][0]['title']
            self.length = jsondoc['movies'][0]['runtime']
            self.critic_rating = jsondoc['movies'][0]['ratings']['audience_score']
            self.thumbnail = jsondoc['movies'][0]['posters']['thumbnail']
            self.actors = jsondoc['movies'][0]['abridged_cast']


class Page(object):  # Borrowing stuff from object class
    def __init__(self):
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self.body = """
        <h1>Search for a Movie</h1>
        """
        self.__result = """

        """
        self.form = """
        <form method="get">
            <input type="text" name="movie" placeholder="Movie Title" />
            <input type="submit" name="Submit" />
        </form>
        """
        self.close = '''
    </body>
</html>'''
        self.whole_page = self.head + self.body + self.form + self.close

    def update(self):
        self.whole_page = self.head + self.body + self.form + self.__result + self.close
        self.whole_page = self.whole_page.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

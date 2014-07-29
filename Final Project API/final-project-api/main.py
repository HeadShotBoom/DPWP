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
        p = FormPage() # This needs to refer to the submost class you are wanting to use

        p.inputs = [['movie', 'text', 'Movie Title'], ['Submit', 'submit']]
        self.response.write(p.print_out())
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

            name = jsondoc['movies'][0]['title']
            length = jsondoc['movies'][0]['runtime']
            critic_rating = jsondoc['movies'][0]['ratings']['audience_score']
            thumbnail = jsondoc['movies'][0]['posters']['thumbnail']
            actors = jsondoc['movies'][0]['abridged_cast']
            this_actor = ""
            count = 0
            for actor in actors:
                this_actor = jsondoc['movies'][0]['abridged_cast'][count]
                count += 1
                print this_actor
            self.response.write("Chosen Movie: " + name + "<br />" + 'The movie is <img src="'+ thumbnail + '" alt="Thumbnail" />')



class Page(object):  # Borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = "Search for a Movie"
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        #Constructor function for super class
        Page.__init__(self)
        self._form_open = '<form method="get">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        # sort through the mega array and create HTML inputs based on info there.
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            # If there is a 3rd Item, add it in
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            # Otherwise end the tag.
            except:
                self._form_inputs += '" />'


    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

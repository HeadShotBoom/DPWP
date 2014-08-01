# Opening Docstring to introduce Myself
"""
Daniel Carroll
DPW - Online
Final Project
July 28, 2014
Booya Grandma
"""
import webapp2
import urllib2 # python classes and code needed to open up url info
import json

# This is the main class that interacts with the browser
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # This needs to refer to the submost class you are wanting to use
        p.inputs = [['movie', 'text', 'Movie Title'], ['Submit', 'submit']]


        if self.request.GET:
            if self.request.GET['movie']!="":
                #get info from the API
                mm = MovieModel()  #Creates Model
                this_movie = self.request.GET['movie'] # Sends Movie from URL to model
                # Uses regular expression to format whitespace for url transmital
                new_movie = this_movie.replace(" ", "+")
                mm.movie = new_movie
                # Sends request to API server
                mm.callApi()
                mv = MovieView()
                # Stores information about current movie in an area where the view controller can use it.
                mv.wdos = mm.current_movie  # Takes data objects from model and gives to view.
                # Replaces the body information with this information.
                p._body = '<h3>The movie you selected is '+ mm.current_movie[0] + \
                          '.</h3> <section><div><h4>Box Image</h4>' + '<img src="' + mm.current_movie[3] \
                          + '" alt="thumbnail" /></div><p class="push">Title: ' + mm.current_movie[0] + '<p>It has a runtime of ' + str(mm.current_movie[1]) + \
                          ' minutes.</p>' + '<p>It has a rating of ' + str(mm.current_movie[2]) + ' .</p>' + \
                          '<p>The main actor is ' + mm.current_movie[4] + ' .</p></section>'
                # Write info to browser
                self.response.write(p.print_out())
            else:
                self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())

# View class of MVC arcitecture
class MovieView(object):
    """
    This class handles how the data is shown to the user.
    """
    def __init__(self):
        # Holds data found from another class
        self.__wdos = []
        # Placeholder for content section.
        self.__content = ""


    # Getter for wdos
    @property
    def wdos(self):
        return self.__wdos
    # Setter for wdos
    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr



# Model class for this project
class MovieModel(object):
    """This model handles fetching parsing and sorting data from rotten tomatoes api """
    def __init__(self):
        # Placeholders
        self.jsondoc = ""
        self.__movie = ""

    # Function used to call the api site and get information from it.
    def callApi(self):
        #get info from the API
        url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=zt3u3utgzsba8qdy3bwcaf6g&q=" + \
              self.__movie + "&page_limit=1"
        #Assemble the request
        request = urllib2.Request(url)
        #Use URLLIB2 Library to create object to get url
        opener = urllib2.build_opener()
        #Use URL to get result - request info from API
        result = opener.open(request)

        #parsoing the json
        jsondoc = json.load(result)

        # Stores specific pieces of information to variables so I can toss it to another class later.
        self.current_movie_title = jsondoc['movies'][0]['title']
        self.current_movie_length = jsondoc['movies'][0]['runtime']
        self.current_movie_critic_rating = jsondoc['movies'][0]['ratings']['audience_score']
        self.current_movie_thumbnail = jsondoc['movies'][0]['posters']['thumbnail']
        self.current_movie_actor = jsondoc['movies'][0]['abridged_cast'][0]['name']
        # Combines all above variables into an object for easy transportation
        self.__current_movie = [self.current_movie_title, self.current_movie_length, self.current_movie_critic_rating, self.current_movie_thumbnail, self.current_movie_actor]

     #getter for current movie
    @property
    def current_movie(self):
        return self.__current_movie

    #setter for current movie
    @current_movie.setter
    def current_movie(self, new):
        self.__current_movie = new
        return self.__current_movie

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie):
        self.__movie = new_movie
        return self.__movie

class MovieData(object):
    """
    This data object holds the data fetched by the model and shown by the view
    """
    def __init__(self):
        self.title = ""
        self.length = ""
        self.critic_rating = ""
        self.thumbnail = ""
        self.actor = ""

class Page(object):  # Borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Movie Search</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self._body = """
        <h3>Enter a Movie above to Search our Database</h3>
        <img src="images/imdb.png" alt="IMDB Logo" />
        """
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

        # print self._form_inputs

    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

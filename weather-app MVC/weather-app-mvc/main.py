
import webapp2
import urllib2 # python classes and code needed to open up url info
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # This needs to refer to the submost class you are wanting to use
        p.inputs = [['movie', 'text', 'Movie Title'], ['Submit', 'submit']]


        if self.request.GET:
            #get info from the API
            mm = MovieModel()  #Creates Model
            this_movie = self.request.GET['movie'] # Sends Movie from URL to model
            new_movie = this_movie.replace(" ", "+")
            mm.movie = new_movie
            mm.callApi()
            mv = MovieView()
            mv.wdos = mm.current_movie  # Takes data objects from model and gives to view.
            p._body = mv.content
            self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())

class MovieView(object):
    """
    This class handles how the data is shown to the user.
    """
    def __init__(self):
        self.__wdos = []
        self.__content = '<h3>The movie you selected is.<h3>'
 #         + ' .</h3>' + '<p>It has a runtime of ' + \
 # md.length + ' minutes.</p>' + '<p>It has a rating of ' + do.critic_rating + ' .</p>' + \
 # '<p>The main actor is ' + do.actor + ' .</p>' + '<h4>Box Image</h4>' +'<img src="' + \
 # do.thumbnail + '" width="20" />'



    @property
    def wdos(self):
        return self.__wdos

    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, arr):
        self.__title = arr

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, arr):
        self.__length = arr

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, arr):
        self.__rating = arr

    @property
    def thumbnail(self):
        return self.__thumbnail

    @thumbnail.setter
    def thumbnail(self, arr):
        self.__thumbnail = arr

    @property
    def thumbnail(self):
        return self.__thumbnail

    @thumbnail.setter
    def thumbnail(self, arr):
        self.__thumbnail = arr


    @property
    def actor(self):
        return self.__actor

    @actor.setter
    def actor(self, new):
        self.__actor = new

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, new):
        self.__content = new



class MovieModel(object):
    """This model handles fetching parsing and sorting data from rotten tomatoes api """
    def __init__(self):
        self.jsondoc = ""
        self.__movie = ""

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

        self.current_movie_title = jsondoc['movies'][0]['title']
        self.current_movie_length = jsondoc['movies'][0]['runtime']
        self.current_movie_critic_rating = jsondoc['movies'][0]['ratings']['audience_score']
        self.current_movie_thumbnail = jsondoc['movies'][0]['posters']['thumbnail']
        self.current_movie_actor = jsondoc['movies'][0]['abridged_cast'][0]['name']

        self.__current_movie = [self.current_movie_title, self.current_movie_length, self.current_movie_critic_rating, self.current_movie_thumbnail, self.current_movie_actor]
    @property
    def current_movie(self):
        return self.__current_movie

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
        <title></title>
    </head>
    <body>'''

        self._body = "Movie Search App"
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


import webapp2
import urllib2 # python classes and code needed to open up url info
# from xml.dom import minidom
from xml.etree.ElementTree import QName
import xml.etree.ElementTree as ET
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # This needs to refer to the submost class you are wanting to use
        """
        Inputs for etree and microdom
        p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]
        """
        p.inputs = [['city', 'text', 'city'], ['country', 'text', 'country'], ['Submit', 'submit']]
        self.response.write(p.print_out())
        if self.request.GET:
            #get info from the API
            city = self.request.GET['city']
            country = self.request.GET['country']
            """
            url for yahoo weather
            url = "http://xml.weather.yahoo.com/forecastrss?q=" + zip
            """
            #Url for openweather for JSON
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country
            #Assemble the request
            request = urllib2.Request(url)
            #Use URLLIB2 Library to create object to get url
            opener = urllib2.build_opener()
            #Use URL to get result - request info from API
            result = opener.open(request)

            #parsoing the json
            jsondoc = json.load(result)

            name = jsondoc['name']
            condition = jsondoc['weather'][0]['description']
            self.response.write("City Chosen: "+ name + "<br/>" + "Weather ar your location: " + condition)


class Page(object):  # Borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = "Weather App"
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
        # <input type="text" value="" name="first_name" placeholder="First Name" />
        # ['first_name', 'text', 'First Name']
        # <input type="text" value="" name="last_name" placeholder="Last Name" />
        # <input type="submit" value="Submit"

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

        print self._form_inputs

    #POLYMORPHISM ALERT!!!!! --------Method Overriding direct replacement of printout function above
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

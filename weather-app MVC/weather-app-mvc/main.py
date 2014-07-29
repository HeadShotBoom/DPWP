
import webapp2
import urllib2 # python classes and code needed to open up url info
from xml.dom import minidom
# from xml.etree.ElementTree import QName
# import xml.etree.ElementTree as ET
# import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # This needs to refer to the submost class you are wanting to use

        p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]
        self.response.write(p.print_out())
        if self.request.GET:
            #get info from the API
            wm = WeatherModel()
            wm.zip = self.request.GET['zip']
            wm.callApi()
            # self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            """
            self.content = '<br/>'
            for item in list:
                self.content += item.attributes['day'].value
                self.content += "     HIGH: "+item.attributes['high'].value
                self.content += "     LOW: "+item.attributes['low'].value
                self.content += "     CONDITION: "+item.attributes['text'].value
                self.content += '<img src="images/'+item.attributes['code'].value+'.png" width="30" />'
                self.content += "<br/>"

            self.response.write(self.content)
            """

class WeatherModel(object):
    """This model handles fetching parsing and sorting data from yahoo weather api """
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?q="
        self.__zip = ""
        self.__xmldoc = ""
        #parse the url


    def callApi(self):
        #Requests and loads info from api
        #Assemble the request
        request = urllib2.Request(self.__url+self.__zip)
        #Use URLLIB2 Library to create object to get url
        opener = urllib2.build_opener()
        #Use URL to get result - request info from API
        result = opener.open(request)
        #Parse DATA
        self.__xmldoc = minidom.parse(result)


        list = self.__xmldoc.getElementsByTagName("yweather:forecast")
        self._dos = []
        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.date = tag.attributes['date'].value
            do.low = tag.attributes['low'].value
            do.code = tag.attributes['code'].value
            do.condition = tag.attributes['text'].value
            self._dos.append(do)

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, new_zip):
        self.__zip = new_zip

class WeatherData(object):
    """
    This data object holds the data fetched by the model and shown by the view
    """
    def __init__(self):
        self.day = ""
        self.high = ""
        self.low = ""
        self.code = ""
        self.condition = ""
        self.date = ""

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

    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

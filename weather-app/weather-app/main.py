
import webapp2
import urllib2 # python classes and code needed to open up url info
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # This needs to refer to the submost class you are wanting to use
        p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]
        self.response.write(p.print_out())
        if self.request.GET:
            #get info from the API
            zip = self.request.GET['zip']
            url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip
            #Assemble the request
            request = urllib2.Request(url)
            #Use URLLIB2 Library to create object to get url
            opener = urllib2.build_opener()
            #Use URL to get result - request info from API
            result = opener.open(request)

            #Parse the xml
            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            self.content = '<br/>'
            list = xmldoc.getElementsByTagName("yweather:forecast")
            for item in list:
                self.content += item.attributes['day'].value
                self.content += "     HIGH: "+item.attributes['high'].value
                self.content += "     LOW: "+item.attributes['low'].value
                self.content += "     CONDITION: "+item.attributes['text'].value
                self.content += "<br/>"

            self.response.write(self.content)

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

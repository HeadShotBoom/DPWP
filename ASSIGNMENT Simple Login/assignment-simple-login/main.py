'''
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Simple Login
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>

    </head>
    <body>
        <form method="GET">
            <label>Name: <input type="text" name="user" /></label>
            <label>Email: <input type="test" name="email" /></label>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>'''
        self.response.write(page) #Prints information to page

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

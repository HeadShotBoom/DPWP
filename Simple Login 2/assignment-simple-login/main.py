'''
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Simple Login
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>

    </head>
    <body>'''

        page_body = '''<form method="GET">
            <label>Name: <input type="text" name="user" /></label>
            <label>Email: <input type="test" name="email" /></label>
            <input type="submit" value="Submit" />'''
        page_close = '''</form>
    </body>
</html>'''
        if self.request.GET:
            #stores info we got from the form
            user =  self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + " " + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #Prints information to page

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


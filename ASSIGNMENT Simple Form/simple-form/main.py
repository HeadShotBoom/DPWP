'''
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Simple Form
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
            <label>Name: <input type="text" name="first" /></label>
            <label>Name: <input type="text" name="last" /></label>
            <label>Email: <input type="test" name="email" /></label>
            <input type="checkbox" name="gender" value="Male">Male<br>
            <input type="checkbox" name="gender" value="Female">Female
            <select name="mood">
                <option value="happy">Happy</option>
                <option value="sad">Sad</option>
                <option value="mad">Mad</option>
                <option value="nervous">Nervous</option>
            </select>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>'''
        if self.request.GET:
            first_name = self.request.GET["first"]
            last_name = self.request.GET["last"]
            email = self.request.GET["email"]
            gender = self.request.GET["gender"]
            birthday = self.request.GET["mood"]
            self.response.write("First Name: " + first_name)
        else:
            self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

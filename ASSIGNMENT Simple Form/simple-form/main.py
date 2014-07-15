'''
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):


    def get(self):
        p = Page()
        self.response.write(p.print_out())


class Page(object):
    def __init__(self):
        self.css = "css/styles.css"

        self.page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>
    <link href="{self.css}" rel="stylesheet" type="text/css" />

    </head>
    <body>'''
        self.first_page = '''
        <h2>Please enter your profile information</h2>
        <form method="GET">
            <label>Name: <input type="text" name="first" /></label>
            <label>Name: <input type="text" name="last" /></label>
            <label>Email: <input type="test" name="email" /></label>
            <input type="checkbox" name="gender" value="Male">Male<br>
            <input type="checkbox" name="gender" value="Female">Female
            <select name="mood">
                <option value="Happy">Happy</option>
                <option value="Sad">Sad</option>
                <option value="Mad">Mad</option>
                <option value="Nervous">Nervous</option>
            </select>
            <input type="submit" value="Submit" />
        </form>'''
        self.page_close = '''
    </body>
</html>'''
        if self.request.GET:
            # first_name = self.request.GET["first"]
            # last_name = self.request.GET["last"]
            # email = self.request.GET["email"]
            # gender = self.request.GET["gender"]
            # mood = self.request.GET["mood"]
            self.second_page = '''<h3>Please Verify Your Information Below</h3>
        <p>Name: ''' + first_name + " " + last_name + '''</p>
        <p>Email: ''' + email + '''</p>
        <p>Gender: ''' + gender + '''</p>
        <p>Mood: ''' + mood + '''</p>
        '''
            self.response.write(self.page_head + self.second_page + self.page_close)
        else:
            self.response.write(self.page_head + self.first_page + self.page_close)

        # def print_out(self):
        #     all = self.head + self.body + self.close
        #     all = all.format(**locals())
        #     return all


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

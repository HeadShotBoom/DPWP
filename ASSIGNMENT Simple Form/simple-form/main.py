'''
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Simple Form
'''
import webapp2 # Inport the WebApp app

class MainHandler(webapp2.RequestHandler): # Single class to handle all the functions of the app


    def get(self): # Single function to handle entire app

        '''
        Below are several variables holding HTML elements that makeup my page. I have broken them down into useful chunks that can be combined and called to make all of my pages
        '''
        self.page_head = """<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>
    <link href="css/styles.css" rel="stylesheet" type="text/css" />

    </head>
    <body>"""
        # Below is the HTML that gets placed under the head of the page upon initial load. It consists of the form and text that collects data from the user.
        self.first_page = """
        <img src="images/logo.png" alt="Yacht" >
        <section>
        <h1>Please enter your profile information</h1>
        <form method="GET">
            <label>First Name: <input type="text" name="first" /></label>
            <label>Last Name: <input type="text" name="last" /></label>
            <label>Email: <input class="push" type="text" name="email" /></label>
            <label>Male<input type="checkbox" name="gender" value="Male"></label>
            <label>Female<input type="checkbox" name="gender" value="Female"></label>
            <select name="mood">
                <option value="Happy">Happy</option>
                <option value="Sad">Sad</option>
                <option value="Mad">Mad</option>
                <option value="Nervous">Nervous</option>
            </select>
            <input type="submit" value="Submit" />
        </form></section>"""
        # This is just the closing tags of the page
        self.page_close = """
    </body>
</html>"""
        self.error = """
        <h1 class="error">You Must Completly Fill Out This Form</h1>
        """
        if self.request.GET:
            if self.request.GET["first"] != "" and self.request.GET["last"] != "" and self.request.GET["email"] != "":
                first_name = self.request.GET["first"]
                last_name = self.request.GET["last"]
                email = self.request.GET["email"]
                gender = self.request.GET["gender"]
                mood = self.request.GET["mood"]
                self.second_page = """<section>
                <h3>Please Verify Your Information Below</h3>
                <p>Name: """ + first_name + " " + last_name + """</p>
                <p>Email: """ + email + """</p>
                <p>Gender: """ + gender + """</p>
                <p>Mood: """ + mood + """</p>
                <input type="button" value="Thats Correct" />
                </section>
                """
                self.response.write(self.page_head + self.second_page + self.page_close)
            else:
                self.response.write(self.page_head + self.error + self.first_page + self.page_close)
        else:
            self.response.write(self.page_head + self.first_page + self.page_close)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

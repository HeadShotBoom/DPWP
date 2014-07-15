"""
Daniel Carroll
14 July 2014
Design Patterns for Web Programming
Simple Form
"""
import webapp2  # Import the WebApp app


class MainHandler(webapp2.RequestHandler):  # Single class to handle all the functions of the app

    def get(self):  # Single function to handle entire app

        """
        Below are several variables holding HTML elements that makeup my page. I have broken them down into useful
        chunks that can be combined and called to make all of my pages
        """
        self.page_head = """<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>
    <link href="css/styles.css" rel="stylesheet" type="text/css" />

    </head>
    <body>"""
        # Below is the HTML that gets placed under the head of the page upon initial load.
        # It consists of the form and text that collects data from the user.
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
        #This is the error message that will load if the user tries to submit blank fields.
        self.error = """
        <h1 class="error">You Must Completely Fill Out This Form</h1>
        """
        # Below is the conditional statement that checks to see if a request has been made from the page.
        if self.request.GET:
            # If a request has been made from the form this conditional statements ensures there are no blank fields
            if self.request.GET["first"] != "" and self.request.GET["last"] != "" and self.request.GET["email"] != "":
                # If there are no blank fields, this code will run.
                # The next 5 lines stores what is entered into the input fields to a variable that I will use later
                # first_name = self.request.GET["first"]
                # last_name = self.request.GET["last"]
                # email = self.request.GET["email"]
                # mood = self.request.GET["mood"]
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + str(self.request.GET)
                test = str([self.request.GET])
                check = test.index("u'gender'")
                print str(check)
                # if str(self.request.GET).index("u'gender'"):
                #     print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
                # else:
                #     print "()()()()()()()()()()()()()()()()()()()()()()()()()("
                # print test
                # if int(test) > 0:
                #     print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ THIS WORKS"
                # else:
                #     print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ THIS DOSENT WORK"
                # This is code that IF a populated request was made will take that info
                # and publish it to the browser.
                # self.second_page = """<section>
                # <h3>Please Verify Your Information Below</h3>
                # <p>Name: """ + first_name + " " + last_name + """</p>
                # <p>Email: """ + email + """</p>
                # <p>Gender: """ + gender + """</p>
                # <p>Mood: """ + mood + """</p>
                # <input type="button" value="Thats Correct" />
                # </section>
                # """
                #  This is the code that concatenates the partial HTML pages and publishes to the browser.
                # self.response.write(self.page_head + self.second_page + self.page_close)
            else:  # If they submit a blank request, this populates the page with an error message
                self.response.write(self.page_head + self.error + self.first_page + self.page_close)
        else:  # If no request has been made, an initial page with blank fields is populated
            self.response.write(self.page_head + self.first_page + self.page_close)

# Don't touch this, its magical and we don't need to know what it does.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

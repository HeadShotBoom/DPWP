class Page(object):

    def __init__(self):
        self.__title = "This Shouldent Be Here"
        self.__css = "ERROR"
        self.__all_cameras = "ERROR"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """


        self.__body = """
        <a href="?cameras=c1">c1</a><br/>
        <a href="?cameras=c2">c2</a><br/>
        <a href="?cameras=c3">c3</a><br/>
        <a href="?cameras=c4">c4</a><br/>
        <a href="?cameras=c5">c5</a><br/>
        """

        self.__display = "Placeholder"

        self.close = """
    </body>
</html>"""
        self.whole_page = ""
        self.__camera = "Not a Camera"

    def update(self):
        if self.__camera == "Not a Camera":
            self.__display = "<h1>No Change</h1>"
        else:
            self.__display = "<h1>Your selected camera is " + self.camera + "</h1>"
        self.whole_page = self.head + self.body + self.display + self.close
        self.whole_page = self.whole_page.format(**locals())

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css):
        self.__css = new_css
        self.update()

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, new_display):
        self.__display = new_display
        self.update()

    @property
    def camera(self):
        return self.__camera

    @camera.setter
    def camera(self, new_camera):
        self.__camera = new_camera
        self.update()

    @property
    def all_cameras(self):
        return self.__all_cameras

    @all_cameras.setter
    def all_cameras(self, new_cameras):
        self.__all_cameras = new_cameras
class Page(object):

    def __init__(self):
        self.__title = "This Shouldent Be Here"
        self.__css = "ERROR"
        self.__current_camera = "ERROR"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """


        self.__body = """<section><img src="images/logo.png" alt="Store Logo" />
        <a href="?cameras=c1">c1</a><br/>
        <a href="?cameras=c2">c2</a><br/>
        <a href="?cameras=c3">c3</a><br/>
        <a href="?cameras=c4">c4</a><br/>
        <a href="?cameras=c5">c5</a><br/>
        """

        self.__display = ""

        self.close = """
    </body>
</html>"""
        self.whole_page = ""
        self.__camera = "Not a Camera"

    def update(self):
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
    def current_camera(self):
        return self.__current_camera

    @current_camera.setter
    def current_camera(self, new_cameras):
        self.__current_camera = new_cameras
        self.__display = """<p>Current Camera Name is: {self.current_camera.name} </p>
        <p>The Body price in this package is: {self.current_camera.body_cost}</p>
        <p>Current Camera Package Lens Value: {self.current_camera.lens_cost}</p>
        <p>Current Camera Package Accessories Cost: {self.current_camera.accessories_cost}</p>
        <p>The reviews have said the quality of this camera is {self.current_camera.quality}.</p>
        <p>The Calculated Value of this total package is: {self.current_camera.value}</p>
        </section>
        """
        self.update()



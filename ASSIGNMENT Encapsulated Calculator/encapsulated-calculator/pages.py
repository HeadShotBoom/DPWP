class Page(object):

    def __init__(self):
        self.__title = "This Shouldent Be Here"
        self.css = "css/styles.css"
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
        <ul>
            <li><a href="?cameras=0">Camera Package 1</a></li>
            <li><a href="?cameras=1">Camera Package 2</a></li>
            <li><a href="?cameras=2">Camera Package 3</a></li>
            <li><a href="?cameras=3">Camera Package 4</a></li>
            <li><a href="?cameras=4">Camera Package 5</a></li>
        </ul>
        """

        self.__display = "<h1 class='Home'>Click One of Our Packages to See Our Current Deals</h1><br/>"
        self.__deal = ""
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
        if self.current_camera.lens_cost >= 0 and self.current_camera.lens_cost <= 500:
            self.lens_package = "images/lenses_small.jpg"
        elif self.current_camera.lens_cost > 500 and self.current_camera.lens_cost <= 2000:
            self.lens_package = "images/lenses_medium.jpg"
        else:
            self.lens_package = "images/lenses_large.jpg"

        if self.current_camera.accessories_cost >= 0 and self.current_camera.accessories_cost <= 50:
            self.accessories_package = "images/accessories_small.jpg"
        elif self.current_camera.accessories_cost > 50 and self.current_camera.accessories_cost <= 200:
            self.accessories_package = "images/accessories_medium.jpg"
        else:
            self.accessories_package = "images/accessories_large.png"

        self.__display = """<article><p>Current Camera Name is: {self.current_camera.name} </p>
        <p>The Body price in this package is: ${self.current_camera.body_cost}</p>
        <p>Current Camera Package Lens Value: ${self.current_camera.lens_cost}</p>
        <p>Current Camera Package Accessories Cost: ${self.current_camera.accessories_cost}</p>
        <p>The reviews have said the quality of this camera is {self.current_camera.quality}.</p>
        <p>The Calculated Value of this total package is: ${self.current_camera.value}</p><br/>
        <img class='deal' src='images/great_deal.jpg' alt='great deal logo' />
        </article>
        <aside>
        <img class='aside' src='images/{self.current_camera.name}.jpg' alt='Camera Body' />
        <div><img class='article' src='{self.lens_package}' alt='Lens Pic' />
        <img class='article' src='{self.accessories_package}' alt='Lens Pic' /></div>

        </aside>
        </section>
        """
        self.update()



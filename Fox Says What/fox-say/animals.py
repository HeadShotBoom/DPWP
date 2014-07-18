class Animal(object):
    def __init__(self):

        self.name = ""
        self.phylum = ""
        self.klass = ""
        self.family = ""
        self.genus = ""
        self.url = ""
        self.lifespan = ""
        self.habitat = ""
        self.geolocation = ""
        self.sound = "audio/jungle.mp3"

class Snake(Animal):
    def __init__(self):
        Animal.__init__(self)

        self.name = "Kobra"
        self.phylum = "Chordata"
        self.klass = "Reptilia"
        self.family = ""
        self.genus = "Varanus"
        self.url = "images/snake.png"
        self.lifespan = "7 Years"
        self.habitat = "Zoo"
        self.geolocation = "Komodo Island"
        self.sound = "audio/snake.mp3"


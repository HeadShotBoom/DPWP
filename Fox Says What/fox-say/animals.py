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

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)

        self.name = "Hummingbird"
        self.phylum = "Chordata"
        self.klass = "Aves"
        self.family = "Trochilidae"
        self.genus = "Selasphorus"
        self.url = "images/hummingbird.jpg"
        self.lifespan = "5 Years"
        self.habitat = "The Sky"
        self.geolocation = "USA"
        self.sound = "audio/hummingbird.mp3"


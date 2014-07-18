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
        self.sound = self.loud_noises()

    def loud_noises(self):
        self.noise = "<audio autoplay src='audio/jungle.mp3' />"
        return self.noise

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
        self.sound = self.loud_noises()

    def loud_noises(self):
        self.noise = "<audio autoplay src='audio/snake.mp3' />"
        return self.noise

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
        self.sound = self.loud_noises()

    def loud_noises(self):
        self.noise = "<audio autoplay src='audio/hummingbird.mp3' />"
        return self.noise


class Person(Animal):
    def __init__(self):
        Animal.__init__(self)

        self.name = "Human Being"
        self.phylum = "Chordata"
        self.klass = "Mammalia"
        self.family = "Hominidae"
        self.genus = "Homo"
        self.url = "images/human.jpg"
        self.lifespan = "80"
        self.habitat = "In Da Club"
        self.geolocation = "On Da Pole"
        self.sound = self.loud_noises()

    def loud_noises(self):
        self.noise = "<audio autoplay src='audio/wrecking_ball.mp3' />"
        return self.noise
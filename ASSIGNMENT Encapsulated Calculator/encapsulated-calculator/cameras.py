# Establishes Cameras Class
class Cameras(object):
    # Initializes Class
    def __init__(self):
        self.name = ""
        self.body_cost = 0
        self.lens_cost = 0
        self.accessories_cost = 0
        self.quality = ""
        self.__value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value
    # Function that calculates the value based on other camera values
    def calc_value(self):
        # Checks the quality attribute and sets a divider variable based on the response
        if self.quality == "High":
            divider = 1
        elif self.quality == "Medium":
            divider = 2
        elif self.quality == "Low":
            divider = 3
        else:
            divider = 10
        # Math
        self.__value = (self.body_cost + self.lens_cost + self.accessories_cost)/divider
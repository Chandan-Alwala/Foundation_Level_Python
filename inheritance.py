#inheritance
class Person:
    def __init__(self, name):
        #self.name = name
        print("check")

    def talk(self):
        print("{} talking".format(self.name))

class Human(Person):
    def think(self):
        print("thinking")
h = Human("check")
p = Person("John")



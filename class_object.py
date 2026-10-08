class student:
    def __init__(self,a,b):
        self.name=a
        self.roll=b

    def read(self):
        print(self.name,"which roll is ",self.roll,"read the book")


c=student("mosaddek",83)
c.read()

d=student("manager",82)
d.read()




class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def show(self):
        print("the car is ",self.brand, "the color is " ,self.color)


a=car("tata","red")
a.show()




class cat:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("the cat is barking",self.name)

a=cat("meow")
a.sound()
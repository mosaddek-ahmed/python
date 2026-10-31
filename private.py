class car:
    def __init__(self,brand):
        self.__brand = brand

class mycar(car):
    def showroom(self):
        return(self.__brand)

a=mycar("Tesla")
print(a.showroom())

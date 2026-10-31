class car:
    def __init__(self,brand):
        self._brand = brand

class mycar(car):
    def showroom(self):
        return(self._brand)

a=mycar("Tesla")
print(a.showroom())

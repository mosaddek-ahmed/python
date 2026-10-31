print("Khabar List")
class Meal():
    def __init__(self,Sokal,Dopor,Rat):
        self.sokal = Sokal
        self.dupur = Dopor
        self.rat = Rat
    def show(self):
        print(f"{self.sokal} {self.dupur} {self.rat}")

Robiber = Meal("Vat","Mach","Dal")
Robiber.show()
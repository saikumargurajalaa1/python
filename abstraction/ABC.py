from abc import ABC,abstractmethod

class CoffeMachine(ABC):
    @abstractmethod
    def click(self):
        pass
class Cappuccino(CoffeMachine):
    def click(self):
        print("cappuccino")
class Expresso(CoffeMachine):
    def click(self):
        print("expresso")
class Coffe(CoffeMachine):
    def click(self):
        print("coffe")
class Milk(CoffeMachine):
    def click(self):
        print("milk")
class Water(CoffeMachine):
    def click(self):
        print("water")
x=Water()
x.click()
x=Milk()
x.click()
x=Expresso()
x.click()
x=Coffe()
x.click()
x=Cappuccino()
x.click()


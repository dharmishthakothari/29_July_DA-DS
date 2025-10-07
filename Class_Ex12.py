from abc import ABC,abstractmethod
class First(ABC):
    # abstract class contains abstract and non abstract methods 
    #abstract method
    @abstractmethod
    def greet(self):
        pass
    #non abstract method
    def bye(self):
        print("BYE")
class Second(First):
   pass
class Third(Second):
    def __init__(self,name):
        self.name=name        
    def greet(self):
        print("Have a nice Day!!!!")
#abstract class can not instatiate / can not create object of Abstract cclass
obj=Third()
obj.greet()
obj.bye()



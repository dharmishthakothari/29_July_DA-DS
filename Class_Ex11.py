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
    #when you exteding abstract class at that time you must have to override/implement abstrat method
    def greet(self):
        print("Good Morning!!!!")
#abstract class can not instatiate / can not create object of Abstract cclass
# obj=Second()
# obj.greet()
# obj.bye()
obj=First()
obj.greet()
obj.bye()

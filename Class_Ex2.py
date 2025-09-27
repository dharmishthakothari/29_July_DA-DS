class Person:
    def getDetails(self,name,age):
       self.name=name
       self.age=age
    def display(self):
        print(f"{self.name} - {self.age}")

obj=Person()
obj.getDetails("Utasav",20)
obj.display()
print(f"{obj.name} - {obj.age} ")


obj1=Person()
obj1.getDetails("Anis",21)
obj1.display()
print(f"{obj1.name} - {obj1.age} ")



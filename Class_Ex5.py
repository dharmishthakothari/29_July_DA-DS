class Vehical:
    def __init__(self,color,price,type):
        self.color=color
        self.price=price
        self.type=type
    def display(self):
        print(f"{self.color} - {self.price} - {self.type}")
class Car(Vehical):
    def __init__(self,brand,model,color, price, type):
        # call super class init 

        super().__init__(color, price, type)
        self.brand=brand
        self.model=model
    def display(self):
        #print(f"{self.brand} - {self.model} - {self.color} - {self.price}")
        super().display()
        print(f"{self.brand} - {self.model} ")

class Scooter(Vehical):
    pass

obj=Car("Hundai","model-2023","white",343434,"EV")
obj.display()

# obj1=Scooter("Activa","Black",34000,"petrol")
# obj1.display()
# multilevel inheritance 
class GrandParents:
    def greet(self):
        print("Hello From GP")
class Parents(GrandParents):
    # method overriding 
    def greet(self):
        super().greet()
        print("Hello From Parent")


class Child(Parents):
    def greet(self):
        super().greet()
        print("Hello from Child")

objChild=Child()
objChild.greet()
print("Creating object of Parents class")
objParent=Parents()
objParent.greet()
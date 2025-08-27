# SOLUTIONS
# (1) =>
 # __init__ is also known as 'constructor' And 'self' is used for refering ourselves.

class Car:
    def __init__(self, userBrand, userModel):      
        self.brand = userBrand   # here 'brand' is a variable of class.
        self.model = userModel   # here 'model' is a variable of class.

    # Makes our own function or defination and we can access constructor values from using self:
    def fullNameOfCar(self):
        return f"{self.brand} {self.model}"

my_car = Car("Mahindra", "Thar") # my_car is a instance, we can make another instances also, when we call pass varibales in Class then they automatically goto __init__ method.
print(my_car.brand) 
print(my_car.model) 
print(my_car.fullNameOfCar())   # using '()' because it is function.

my_new_car = Car("Tata", "Punch");
print(my_new_car.brand) 
print(my_new_car.model) 



# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# (2) => Inheritance::
class Car2:
    def __init__(self, brand, model):      
        self.brand = brand   
        self.model = model  

    def fullNameOfCar(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car2):                            # inherit 'Car2' class
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)              # we can use attributes and function in our own class of our inherited Class by using super().
        self.batterySize = batterySize


my_electic_car = ElectricCar("Mahindra", "Scorpio", "85KWh")
print(my_electic_car.brand)
print(my_electic_car.fullNameOfCar())

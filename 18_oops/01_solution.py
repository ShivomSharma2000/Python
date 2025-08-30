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
# print(my_car.brand) 
print(my_car.model) 
print(my_car.fullNameOfCar())   # using '()' because it is function.

my_new_car = Car("Tata", "Punch");
# print(my_new_car.brand) 
print(my_new_car.model) 


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# (3) => Inheritance::
class Car2:
    total_objects = 0

    def __init__(self, brand, model):      
        self.__brand = brand   # (4) it is private, so only in this class can access it and for access it's outside you have to give access using get method. here 'brand' is a variable of class.        
        self.__model = model  
        Car2.total_objects += 1
    
    def get_brand(self):            # (4) like this function we can access private data (this is also called 'Encapsulation')
        return self.__brand + '!'
    
    def set_brand(self, model):            
        if model == 'tata':
            self.__brand = 'punch'
    
    def fuelType(self):            
        return 'Petrol or Desiel'

    def fullNameOfCar(self):
        return f"{self.__brand} {self.__model}"
    
    # this is 'static method', now only Class can access this function rather than 'objects' and also now don't need to use 'self' arguments because now we don't need to connect it's for objects.
    @staticmethod               # This is decorator
    def general_description():            
        return 'Cars are amazing.'
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car2):                            # inherit 'Car2' class
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)              # we can use attributes and function in our own class of our inherited Class by using super().
        self.batterySize = batterySize
    
    def fuelType(self):            
        return 'Electric charge'


my_electic_car = ElectricCar("Mahindra", "Scorpio", "85KWh")
# print(my_electic_car.__brand)     we can't access __brand because it is private.
print(my_electic_car.set_brand('tata'))
print(my_electic_car.get_brand())
print(my_electic_car.fullNameOfCar())

my_thar = Car2("Tata", "Punch");

# (5) This is the e.g of 'Polymorphism' (poly means 'many' and morphism means 'identity(roops in hindi)'), we used same function name but in different objects.
print(my_electic_car.fuelType());
print(my_thar.fuelType());      

# (6) How we get to know that how many objects made for given class
print(Car2.total_objects)

# (7) Sometimes, We also wants to get data by using 'Class' only rather than object, So in that case we are making 'static methods'.
# print(my_thar.general_description())  
print(Car2.general_description())


# (8) If you don't want to override any value so in that case we have to use 'Property' decorators, so by using this method we can't override any value.
print(my_thar.model)

# (9) Use isinstance() to check if my_electic_car is an instance of Car2 and ElectricCar.
print(isinstance(my_electic_car, Car2))
print(isinstance(my_electic_car, ElectricCar))


# (10) Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"
    
class ElectricCarTwo(Battery, Engine, Car2):        # here we inherit two classes.
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")           # this argument passes on Car2 class.
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())


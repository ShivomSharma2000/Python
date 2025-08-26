# SOLUTIONS
# (1) =>
 # __init__ is also known as 'constructor' And 'self' is used for refering ourselves.

class Car:
    def __init__(self, userBrand, userModel):      
        self.brand = userBrand   # here 'brand' is a variable of class.
        self.model = userModel   # here 'model' is a variable of class.

my_car = Car("Mahindra", "Thar") # my_car is a instance, we can make another instances also, when we call pass varibales in Class then they automatically goto __init__ method.
print(my_car.brand) 
print(my_car.model) 


my_new_car = Car("Tata", "Punch");
print(my_new_car.brand) 
print(my_new_car.model) 

# ---------------------------------------------------------------------------------------
# (2) => 


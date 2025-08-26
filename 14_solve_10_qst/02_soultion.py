age= int(input("Enter your age: "))
day= input("Day is: ")

price= 12 if age >= 18 else 8

if day == 'Wednesday':
    price = price - 2;

print("Ticket price for you is $",price);
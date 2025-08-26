user_age= input("Enter your Age: ");
user_age_int= int(user_age);

if(user_age_int < 13):
    print("Child")

elif(user_age_int < 20):
    print("Teenager")

elif(user_age_int < 60):
    print("Adult")

else:
    print("Senior")
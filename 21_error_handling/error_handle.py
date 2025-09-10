# How to make file and also write down something (This is the older way where you have to make sure to use try and finally for handling):
file = open('youtube.txt', 'w')       # 'w' means write or make the file if don't exist.

try:
    file.write("cahi aur code")       # add someting in file
finally:
    file.close()                      # you have to close this file.


# Now, you can handle it by using 'with' keyword as below(newer way and useful):
with open('youtube.txt', 'w') as file:
    file.write("chai aur python")
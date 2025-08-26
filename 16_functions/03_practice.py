# Funtion with *args:
# Write a function that takes variable number of arguments and return their sum.
# (a) When we don't know how many agruments can pass in function then we have to use '*args', which are handle 
# all the arguments.
# (b) Also, if we are not using '*args' then in agrs only we are getting tuple, so if we don't want to use inbuilt function sum(), instead of this we can use loop.

def sum_all(*args):
    # for i in args:
    #     print(i, "* 2: ", i * 2);
    return sum(args);

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))

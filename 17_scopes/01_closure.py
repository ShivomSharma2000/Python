# Closure
# (a). Here in inner function we are holding reference's of the variable's which are using.
x = 99

def f1():
    x = 88
    def f2(y):
        return x+y
    return f2

result = f1()
print(result)
print(result(2))
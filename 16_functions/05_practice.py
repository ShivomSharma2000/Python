# Generator function with yeild:
# Problem: Write a generator function that yeilds even number up to a specific limit.

# Answer: yield is like a return, but it remembers the function’s state so you can keep getting the next value without restarting the function. It also keeps in mind (or store in memory) that which function called, So it can handle different function states and yield(like a return) individual data.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

# yield keeps data in their memory for both loops individually:
for value in even_generator(10):
    print(value)

for value in even_generator(20):
    print(value)
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time();
        result = func(*args, **kwargs);
        end = time.time();
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer                      # we makes timer name 'decorator' where if you call example_function then initially your time decorator will call and it takes your whole function with arguments.
def example_function(n):
     time.sleep(n)

example_function(2)
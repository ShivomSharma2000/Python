import time


def cache(func):
        cache_value = {}
        print("cache_value",cache_value)

        def wrapper(*args):
                print("args: ",args)
                if args in cache_value:
                        return cache_value[args]
                
                result = func(*args)
                print("result: ",result)
                cache_value[args] = result   # here our key is (2,3) and value is 5.
                return result
            
        return wrapper

@cache
def long_running_function(a, b):
        time.sleep(4)
        return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
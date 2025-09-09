
def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ','.join(str(arg) for arg in args) if args else '0'
        kwargs_values = ','.join(f"{k}:{w}" for k, w in kwargs.items()) if kwargs else '0'

        print(f"'{func.__name__}' function name with args= {args_values} and kwargs={kwargs_values}")
        return func(*args, **kwargs)

    return wrapper


@debug
def forYou(chai, greeting="hello"):
    print(f"{greeting}, {chai}")

@debug
def justGreet():
    print("hello")

forYou('Adrak tea', greeting='Hey')
justGreet()


# Funtion with **kwargs: (key word arguments)
# Create a function that accepts any number of keyword arguments and prints them in the format key:value.
# (a) kwargs.items() converts arguments into dictionary in (key, value) pair.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "shaktiman", power = "range");
print_kwargs(name = "shaktiman");
print_kwargs(name = "shaktiman", power = "range", villian = "Dr. Jackaal");

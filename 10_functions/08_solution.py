# <details>
# <summary>
# 8. Function with **kwargs
# </summary>
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# </details>


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    # print(kwargs)
print_kwargs(name="shaktiman",power="lazer")
print_kwargs(name="shaktiman",power="lazer",enemy="Dr. jackaal")
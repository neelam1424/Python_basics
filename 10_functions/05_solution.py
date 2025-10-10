# <details>
# <summary>
# 5. Default Parameter Value
# </summary>
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
# </details>


def greet(name="Man"):
    return "Hello, "+name+" !"

print(greet("Neelam"))
print(greet())
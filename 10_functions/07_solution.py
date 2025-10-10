# <details>
# <summary>
# 7. Function with *args
# </summary>
# Problem: Write a function that takes variable number of arguments and returns their sum.
# </details>


def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)
print(sum_all(1,2,3))
# <details>
# <summary>
# 10. Recursive Function
# </summary>
# Problem: Create a recursive function to calculate the factorial of a number.
# </details>

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
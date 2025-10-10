# <details>
# <summary>
# 6. Factorial Calculator
# </summary>
# Problem: Compute the factorial of a number using a while loop.
#

# </details>


num=int(input("Enter number"))
fact=1

while num>0:
    fact *= num
    num -=1
print(fact)
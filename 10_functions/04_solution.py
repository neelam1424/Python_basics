# <details>
# <summary>
# 4. Function Returning Multiple Values
# </summary>
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
# </details>

import math
def circle(radius):
    area= math.pi * radius **2
    circumference=2*math.pi*radius
    return area, circumference

a,c=circle(3)

print("Area of circle : ",a," and circumference of circle : ",c)

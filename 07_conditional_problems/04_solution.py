# <details>
# <summary>4. Fruit Ripeness Checker
# </summary>
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

# </details>

fruit = input("Enter your fruit : ")
color = input("Enter color of the fruit : ")

if fruit=="Banana":
    if color =="Green":
        print("Unripe")

    elif color=="Yellow":
        print("Ripe")
    elif color=="Brown":
        print("Overripe")
else:
    print("I have no information of this fruit")
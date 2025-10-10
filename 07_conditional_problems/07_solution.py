# <details>
# <summary>7. Coffee Customization
# </summary>
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# </details>

order_size = input("Enter size of coffee : ")
extra_shot= int(input("Enter 1 for extra shot or enter 0 : "))

if extra_shot:
    coffee=order_size+" coffe with an extra shot"
else:
    coffee=order_size

print("Order: ",coffee)
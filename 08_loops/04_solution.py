# <details>
# <summary>
# 4. Reverse a String
# </summary>
# Problem: Reverse a string using a loop.

# </details>


input_str=input("Enter your string to reverse : ")
reversed_str =""

for char in input_str:
    reversed_str = char+reversed_str
print(reversed_str)
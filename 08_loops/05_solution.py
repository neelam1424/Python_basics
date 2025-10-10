# <details>
# <summary>
# 5. Find the First Non-Repeated Character
# </summary>
# Problem: Given a string, find the first non-repeated character.

# </details>

input_str=input("Enter string")

for char in input_str:
    print(char)
    if input_str.count(char)==1:
        print("Char is : ",char)
        break
 

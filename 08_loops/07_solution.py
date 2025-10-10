# <details>
# <summary>
# 7. Validate Input
# </summary>
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# </details>


while True:
    input_num=int(input("Enter number between 1 and 10 : "))
    if 1<=input_num<=10:
        print("Thanks")
        break
    else:
        print("Invalid number")

    

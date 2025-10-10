# <details>
# <summary>2. Movie Ticket Pricing
# </summary>
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# </details>


# long way
# age=int(input("Enter your age"))
# day=input("Enter day : ")

# if day=="wednesday":
#     if age>=18 :
#         price = 12 
#         discount= price-2
#         print(f'The ticke amount originally is {price} , but as it is wednesday price is {discount}')
#     else:
#         price = 8
#         discount =price-2
#         print(f'The ticke amount originally is ${price} , but as it is wednesday price is ${discount}')

# else:
#     if age>=18:
#         print("price is $12")
#     else:
#         print("price is $8")

age=int(input("Enter your age"))
day=input("Enter day : ")

price = 12 if age>=18 else 8

if day=="Wednesday":
    price =price-2

print("Ticket price for you is $",price)
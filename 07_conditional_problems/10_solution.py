# <details>
# <summary>10. Pet Food Recommendation
# </summary>
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# </details>

species=input("Pet species : ")
age=int(input("Enter pet age : "))

if species=="Dog" :
    if age<2:
        food ="Puppy food"
    else:
        food ="Senior Dog food"

elif species=="Cat":
    if age >5:
        food ="Senior cat food"
    else:
        food="Kitten food"

else:
    food="Unknown pet food"

print("The species of your pet is ",species,"and age is ",age," Give them ",food)

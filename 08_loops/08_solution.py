# <details>
# <summary>
# 8. Prime Number Checker
# </summary>
# Problem: Check if a number is prime.
# prime number greater by 1 which is only divisible by itself
# </details>

number=int(input("Enter your number"))
is_prime=True

if number>1:
    for i in range(2,number+1):
        if (number%i)==0:
            is_prime=False
            break
print(is_prime)
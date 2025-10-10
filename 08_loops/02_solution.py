# <details>
# <summary>
# 2. Sum of Even Numbers
# </summary>
# Problem: Calculate the sum of even numbers up to a given number n.

# </details>

n=int(input("Enter n numbers : "))
sum_even=0

for i in range(1,n+1):
    if(i%2==0):
        sum_even +=i
print("Sum of even numbers till ",n," is : ",sum_even)
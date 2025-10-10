# <details>
# <summary>
# 3. Multiplication Table Printer
# </summary>
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# </details>


n = int(input("Enter number to display multiplication table : "))
print("Starting table...")

for i in range(1,11):
    if i == 5:
        continue
    print(n, " X ", i, " = ", n*i)


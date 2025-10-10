# <details>
# <summary>9. Leap Year Checker
# </summary>
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# </details>

year=int(input("Enter year to check leap year or not : "))

if (year % 400==0) or (year %4==0 and year % 100 !=0): 
    print(year," Year is leap year")
else:
    print(year," Year is Not a leap year")
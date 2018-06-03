# Practise Python
# Project Divisor, exercise 4
# 22 May 2018

print("Hello! I'll tell you all the divisor of any number you'd like!")
number=int(input("What number would you like to check?"))

comparable = list(range(1, number+1))

divs=[]

for num in comparable:
    if number % num == 0:
        divs.append(num)

print("Here is a list of all divisors:")
print(divs)
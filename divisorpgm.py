# Practise Python
# Furthering the idea of Project Divisor, exercise 4
# 22 May 2018

def divisors(x):
    compared = list(range(1,x+1))
    for num in compared:
        if x % num == 0:
            divs.append(num)
    print(divs)
    divs.clear()

divs=[]

print("Hello... this is an attempt to make the divisors program repeatable within a same instance...")
number=int(input("So, what number would you like to check?"))

divisors(number)

print("let's try another...")
newnum=int(input("what next?"))

divisors(newnum)

# Practise Python
# Project List Less Than Ten, exercise 3
# 21 May 2018

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Adds the numbers to a list.

def less5(x):
    fiveLess = []
    for num in x:
        if num <5:
            fiveLess.append(num)
    print(fiveLess)

# Just prints the numbers out.

def pnt5(b):
    for num in b:
        if num <5:
            print(num)

# Uses user input to determine the compared number; puts in a new list.

def lst(y):
    lst5 = []
    for num in y:
        if num <number:
            lst5.append(num)
    print(lst5)


number=int(input("What is the highest number that you want?"))
lst(a)
pnt5(a)
less5(a)
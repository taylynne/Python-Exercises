# Practise Python
# Project List Comprehensions, exercise 07
# 3 June 2018
# notes~
# A list comprehension consists of brackets containing an expression followed by a for clause
# so, *x* for x in a if x blah blah blah....
# or, using python doc example: (x,y) for x in [list] for y in [list] blah blah blah....
# Definitely feel like this is one to revisit in the future

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = []

for x in a:
    if x % 2 == 0:
        even.append(x)

print(even)

# comprehension...

evenNum = [x for x in a if x % 2 == 0]

print(evenNum)
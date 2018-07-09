# Practise Python
# Project List Overlap Comprehensions, exercise 10
# 9 June 2018
# apparently a revist of sorts to a previous exercise.

import random

# create random lists

a = list(random.sample(range(1, 100), 12))
b = list(random.sample(range(20, 88), 18))

# list comprehension...

combinedList = [item for item in a if item in b]

noDupli = [item for item in combinedList if combinedList.count(item) == 1]

print(a)
print(b)
print(combinedList)
print(noDupli)
# Practise Python
# Project List Overlap, exercise 05
# 29 May 2018
# try bonus later... w/ random lists.

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for letter in a:
    if letter in c:
       continue
    else letter in b:
        c.append(letter)

print(c)

# Practise Python
# Project String Lists, exercise 06
# 3 June 2018
# not too sure why this one was so hard for me...
# come back and try to create with loops -- which is what I initially tried to do, but failed.


print("Hello, this is a palindrome 'checker' of sorts...")
paliTest = str(input("So, what word would you like to check?"))

reverse = paliTest[::-1]  # need to keep this last bit in mind, had to see that in results to simplify my solution...
# print(reverse)
if reverse == paliTest:
    print("Good news! " + paliTest.capitalize() + " is a palindrome")
else:
    print("Aww, too bad... " + paliTest.capitalize() + " isn't a palindrome. :(")


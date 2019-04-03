'''

Question: 44

2.14

Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.

'''

yes_no = input("Please type yes or no: ")

print("Yes" if yes_no.lower() == "yes" else "No")


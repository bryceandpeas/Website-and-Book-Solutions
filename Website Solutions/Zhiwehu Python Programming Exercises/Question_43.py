'''

Question: 43

2.10

Question:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.

'''

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(*(i for i in tup if i % 2 == 0))


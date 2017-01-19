"""

Monday 25th April 2016

Hackerrank - XML - XML 1 - Find the Score

You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

Input Format

The first line contains NN, the number of lines in the XML document.
The next NN lines follow containing the XML document.

Output Format

Output a single line, the integer score of the given XML document.


"""

N = int(input())

c = 0

for i in range(N):
    tree = input()

    for j in tree:
        if j == '=':
            c += 1

print (c)




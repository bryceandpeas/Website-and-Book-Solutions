'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Basic Data Types: https://www.hackerrank.com/domains/python/py-basic-data-types

Hackerrank - Python - Basic Data Types - Finding the percentage


You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output

56.00
Explanation

Marks for Malika are  whose average is

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
l = list()
d = dict()

for i in range(N):
    dat = raw_input()
    l = dat.split()
    sdat = l[0]
    l.remove(l[0])

    nl = list(map(float, l))
    d[sdat] = nl

name = raw_input()

t = 0

if name in d:
    marks = d[name]
    n = len(marks)
    for number in marks:
        t += number

average = (t / n)

print '%.2f' % average






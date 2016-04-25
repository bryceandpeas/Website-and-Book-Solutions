"""

February 2016

Hackerrank - Python - Introduction - Finding the Percentage

You have a record of NN students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer NN followed by the names and marks for NN students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer NN, the number of students. The next NN lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


"""

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
    








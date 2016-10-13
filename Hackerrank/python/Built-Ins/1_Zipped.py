"""

Monday 25th April 2016

Hackerrank - Built-Ins - Zipped!

zip([iterable, ...])

This function returns a list of tuples. The iith tuple contains the iith element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

Sample Code

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
Task

The National University conducts an examination of NN students in XX subjects. 
Your task is to compute the average scores of each student.

Average score=Sum of scores obtained in all subjects by a studentTotal number of subjects
Average score=Sum of scores obtained in all subjects by a studentTotal number of subjects
The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
Input Format

The first line contains NN and XX separated by a space. 
The next XX lines contains the space separated marks obtained by students in a particular subject.

Constraints

0<N≤1000<N≤100 
0<X≤1000<X≤100
Output Format

Print the averages of all students on separate lines.

The averages must be correct up to 11 decimal place.

"""





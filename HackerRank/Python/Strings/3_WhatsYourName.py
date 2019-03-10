"""

February 2016

Hackerrank - Python - Introduction - What's Your Name?

Let's learn the basics of Python! You are given the first and last name of a person. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
It's that simple!

In Python, you can read a line as a string using:

s = raw_input()
#here s reads the whole line.
Input Format
The first line contains the first name, and the second line contains the last name.

Constraints
The length of the first and last name ≤ 1010.

Output Format
Print the output as mentioned above.


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

STDFIR = raw_input()
STDSEC = raw_input()

print ('Hello ' + STDFIR + ' ' + STDSEC + '! ' + 'You just delved into python.')




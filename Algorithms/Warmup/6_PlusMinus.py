'''

Hackerank Domains: https://www.hackerrank.com/domains

Algorithms https://www.hackerrank.com/domains/algorithms

Warmup: https://www.hackerrank.com/domains/algorithms/warmup/

Hackerrank - Algorithms - Plus Minus

Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array. 
The respective fractions of positive numbers, negative numbers and zeroes are ,  and , respectively.

contact: bryce@brycefury.com

'''

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


number_of_zeros = 0 
number_of_positives = 0
number_of_negatives = 0

zero_percentage = 0
positive_percentage = 0
negative_percentage = 0

for i in arr:
    if i == 0:
        number_of_zeros += 1
    elif i > 0:
        number_of_positives += 1
    else:
        number_of_negatives += 1

        
zero_percentage = number_of_zeros / float(n)
positive_percentage = number_of_positives / float(n)
negative_percentage = number_of_negatives / float(n) 

print (round(positive_percentage,6))
print (round(negative_percentage,6))
print (round(zero_percentage,6))

'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/tutorials/30-days-of-code

Hackerrank - 30 Days Of Code -  Day 7: Arrays

Objective 
Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.

Input Format

The first line contains an integer,  (the size of our array). 
The second line contains  space-separated integers describing array 's elements.

Constraints

, where  is the  integer in the array.
Output Format

Print the elements of array  in reverse order as a single line of space-separated numbers.

Sample Input

4
1 4 3 2
Sample Output

2 3 4 1

contact: bryce@brycefury.com

'''

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_rev = arr[::-1]


print (' '.join([''.join(str(arr_rev[i])) for i in range(0, len(arr_rev))]))

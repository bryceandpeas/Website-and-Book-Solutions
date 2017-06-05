:'

Hackerank Domains: https://www.hackerrank.com/domains

Linux Shell https://www.hackerrank.com/domains/shell/bash

Bash Challenges: https://www.hackerrank.com/domains/shell/bash

Hackerrank - Linux Shell  - Bash - The World of Numbers

Given two integers,  and , find their sum, difference, product, and quotient.

Input Format

Two lines containing one integer each ( and , respectively).

Constraints



Output Format

Four lines containing the sum (), difference (), product (), and quotient (), respectively.
(While computing the quotient, print only the integer part.)

Sample Input

5
2
Sample Output

7
3
10
2
Explanation

5 + 2 = 7
5 - 2 = 3
5 * 2 = 10
5 / 2 = 2 (Integer part)

Submissions: 25456
Max Score: 2
Difficulty: Easy
Rate This Challenge:

More
Current Buffer (saved locally, editable)



'

read x; read y; printf "%s\n" $x' '{+,-,*,/}' '$y | bc

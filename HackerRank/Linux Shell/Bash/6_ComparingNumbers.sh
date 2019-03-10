:'

Hackerank Domains: https://www.hackerrank.com/domains

Linux Shell https://www.hackerrank.com/domains/shell/bash

Bash Challenges: https://www.hackerrank.com/domains/shell/bash

Hackerrank - Linux Shell  - Bash - Comparing Numbers

Given two integers,  and , identify whether  or  or .

Exactly one of the following lines:
- X is less than Y
- X is greater than Y
- X is equal to Y

Input Format

Two lines containing one integer each ( and , respectively).

Constraints

-

Output Format

Exactly one of the following lines:
- X is less than Y
- X is greater than Y
- X is equal to Y

Sample Input

Sample Input 1

5
2
Sample Input 2

2
2
Sample Input 3

2
3
Sample Output

Sample Output 1

X is greater than Y
Sample Output 2

X is equal to Y
Sample Output 3

X is less than Y
Explanation

-



'

read x; read y;
if  (( $x > $y )); then echo "X is greater than Y"
elif (( $x == $y )); then echo "X is equal to Y"
else (( $x < $y )); echo "X is less than Y"
fi

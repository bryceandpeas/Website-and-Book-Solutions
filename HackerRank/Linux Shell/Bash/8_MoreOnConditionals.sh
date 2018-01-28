:'

Hackerank Domains: https://www.hackerrank.com/domains

Linux Shell https://www.hackerrank.com/domains/shell/bash

Bash Challenges: https://www.hackerrank.com/domains/shell/bash

Hackerrank - Linux Shell  - Bash - More on Conditionals

Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is Scalene, Isosceles, or Equilateral.

Input Format

Three integers, each on a new line.

Constraints


Sum of any two sides will be greater than the third.

Output Format

One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

Sample Input

Sample Input 1

2
3
4
Sample Input 2

6
6
6
Sample Output

Sample Output 1

SCALENE
Sample Output 2

EQUILATERAL
Explanation

-



'

read x; read y; read z;
if (( $x == $y  &&  $x == $z  &&  $z == $y )); then echo "EQUILATERAL"
elif (( $x == $y  ||  $x == $z  ||  $z == $y )); then echo "ISOSCELES"
else echo "SCALENE"
fi

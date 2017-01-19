/*

Hackerank Domains: https://www.hackerrank.com/domains

C++ https://www.hackerrank.com/domains/cpp/

Introduction Challenges: https://www.hackerrank.com/domains/cpp/cpp-introduction

Hackerrank - C++ - Introduction Challenges - Conditional Statements

if and else are two of the most heavily used conditionals in C/C++. They are used to execute zero or one statement among many statements.

They can be used in the following three ways.

if: It is used to execute a statement, given the condition is true.

if(condition) {
    ...
}
if - else: It is used to execute exactly one of the two statements.

if(first condition) {
    ...
}
else {
    ...
}
if - else if - else: It is used to execute one of the multiple statements.

if(first condition) {
    ...
}
else if(second condition) {
    ...
}
.
.
.
else if((n-1)'th condition) {

}
else {
    ...
}
You are given a positive integer, ,:

If , then print the English representation of it. That is "one" for 1, "two" for 2, and so on.
Otherwise print "Greater than 9" (without quotes).
Input Format

Input will contain only one integer, .

Constraints


Output Format

Print the output as described above.

Sample Input

5
Sample Output

five
Sample Input #01

8
Sample Output #01

eight
Sample Input #02

44
Sample Output #02

Greater than 9

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    if(n==1){
        cout << "one";
    }
    else if(n==2){
        cout << "two";
    }
    else if(n==3){
        cout << "three";
    }
    else if(n==4){
        cout << "four";
    }
    else if(n==5){
        cout << "five";
    }
    else if(n==6){
        cout << "six";
    }
    else if(n==7){
        cout << "seven";
    }
    else if(n==8){
        cout << "eight";
    }
    else if(n==9){
        cout << "nine";
    }
    else if(n>9){
        cout << "Greater than 9";
    }

   return 0;
}



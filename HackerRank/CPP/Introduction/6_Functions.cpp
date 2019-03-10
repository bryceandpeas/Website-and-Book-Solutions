/*

Hackerank Domains: https://www.hackerrank.com/domains

C++ https://www.hackerrank.com/domains/cpp/

Introduction Challenges: https://www.hackerrank.com/domains/cpp/cpp-introduction

Hackerrank - C++ - Introduction Challenges - Functions

Functions are a bunch of statements glued together. A function is provided with zero or more arguments, and it executes the statements on it. Based on the return type, it either returns nothing (void) or something.

A sample syntax for a function is

return_type function_name(arg_type_1 arg_1, arg_type_2 arg_2, ...) {
    ...
    ...
    ...
    [if return_type is non void]
        return something of type `return_type`;
}
For example, a function to read four variables and return the sum of them can be written as

int sum_of_four(int a, int b, int c, int d) {
    int sum = 0;
    sum += a;
    sum += b;
    sum += c;
    sum += d;
    return sum;
}
You have to write a function int max_of_four(int a, int b, int c, int d) which reads four arguments and returns the greatest of them.

Input Format

Input will contain four integers -  , one in each line.

Output Format

Print the greatest of the four integers.
PS: I/O will be automatically handled.

Sample Input

3
4
6
5
Sample Output

6

*/

#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
        int answer = 0;
        if(a>answer){
            answer = a;
        }
        if(b>answer){
            answer = b;
        }
        if(c>answer){
            answer = c;
        }
        if(d>answer){
            answer = d;
        }
        return answer;
    }

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}


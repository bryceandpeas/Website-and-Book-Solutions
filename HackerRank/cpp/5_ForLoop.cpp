/*

Hackerank Domains: https://www.hackerrank.com/domains

C++ https://www.hackerrank.com/domains/cpp/

Introduction Challenges: https://www.hackerrank.com/domains/cpp/cpp-introduction

Hackerrank - C++ - Introduction Challenges - For Loop

A for loop is a programming language statement which allows code to be repeatedly executed.

The syntax for this is

for ( <expression_1> ; <expression_2> ; <expression_3> )
    <statement>
expression_1 is used for intializing variables which are generally used for controlling terminating flag for the loop.
expression_2 is used to check for the terminating condition. If this evaluates to false, then the loop is terminated.
expression_3 is generally used to update the flags/variables.
A sample loop will be

for(int i = 0; i < 10; i++) {
    ...
}
Input Format

You will be given two positive integers,  and  (), separated by a newline.

Output Format

For each integer  (so all numbers in that range):

If , then print the English representation of it. That is "one" for 1, "two" for 2, and so on.
Else if  and it is even, then print "even".
Else if  and it is odd, then print "odd".
Note:  represents the interval, i.e., 

Sample Input

8
11
Sample Output

eight
nine
even
odd

*/

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a;
    int b;
    int i;
    cin>>a;
    cin>>b;
    if(b>9) { 
        for(i=a;i<=9;i++) { 
            if(i==2) cout<<"two\n"; 
            else if(i==1) cout<<"one\n"; 
            else if(i==3) cout<<"three\n"; 
            else if(i==4) cout<<"four\n"; 
            else if(i==5) cout<<"five\n"; 
            else if(i==6) cout<<"six\n"; 
            else if(i==7) cout<<"seven\n"; 
            else if(i==8) cout<<"eight\n"; 
            else if(i==9) cout<<"nine\n"; }
        for(int j=10;j<=b;j++){
            if(j%2==0){
                cout<<"even\n";    
                }
            else
                cout<<"odd\n";
        }
    } 
    else { 
        for(i=a;i<=b;i++) { 
            if(i==2) cout<<"two\n"; 
            else if(i==1) cout<<"one\n"; 
            else if(i==3) cout<<"three\n"; 
            else if(i==4) cout<<"four\n"; 
            else if(i==5) cout<<"five\n"; 
            else if(i==6) cout<<"six\n"; 
            else if(i==7) cout<<"seven\n"; 
            else if(i==8) cout<<"eight\n"; 
            else if(i==9) cout<<"nine\n"; }
    }


    return 0;
}


/*

Hackerank Domains: https://www.hackerrank.com/domains

C++ https://www.hackerrank.com/domains/cpp/

Introduction Challenges: https://www.hackerrank.com/domains/cpp/cpp-introduction

Hackerrank - C++ - Introduction Challenges - Variable Sized Arrays

Consider an -element array, , where each index  in the array
contains a reference to an array of  integers (where the value of
varies from array to array). See the Explanation section below for a diagram.

Given , you must answer  queries. Each query is in the format i j,
where denotes an index in array  and  denotes an index in the array
located at . For each query, find and print the value of element  in
the array at location  on a new line.

Click here to know more about how to create variable sized arrays in C++.

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n,q,k,i,j;
    cin >> n >> q;
    vector<vector<int> >arr(n);
    for (i=0; i<n; ++i){
        cin >> k;
        arr[i].resize(k);
        for(j=0 ; j<k; ++j){
            cin >> arr[i][j];
        }
    }

    for(int l=0; l<q; ++l){
        cin >> i >> j;
        cout << arr[i][j]<<endl;
    }
    return 0;
}

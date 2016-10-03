"""

Monday 25th April 2016

Hackerrank - Python - Setss - No Idea!

There is an array of nn integers. There are also 22 disjoint sets, AA and BB, each containing mm integers. You like all the integers in set AA and dislike all the integers in set BB. Your initial happiness is 00. For each ii integer in the array, if i∈Ai∈A, you add 11 to your happiness. If i∈Bi∈B, you add −1−1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since AA and BB are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints 
1≤n≤1051≤n≤105 
1≤m≤1051≤m≤105 
1≤Any integer in the input≤1091≤Any integer in the input≤109

Input Format

The first line contains integers nn and mm separated by a space. 
The second line contains nn integers, the elements of the array. 
The third and fourth lines contain mm integers, AA and BB, respectively.

Output Format

Output a single integer, your total happiness.


"""


N = input()

M = [int(i) for i in input().split()]
A = {int(i) for i in input().split()}
B = {int(i) for i in input().split()}

r = 0

for i in M:
    r+=(i in A)-(i in B)
    
print(r)


    





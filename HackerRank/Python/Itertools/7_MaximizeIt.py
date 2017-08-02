'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Itertools: https://www.hackerrank.com/domains/python/py-itertools

Hackerrank - Python - Itertools - Maximize It!

You are given a function .

You are also given  lists. The  list consists of  elements.

You have to pick exactly one element from each list so that the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Input Format
The first line contains  space separated integers  and .
The next  lines each contains an integer  followed by  space separated integers denoting the elements in the list.

Output Format
Output a single integer denoting the value .

Constraints




Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output

206
Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .

'''

from itertools import product

K, M = map(int, input().split(' '))

def solver(K, M):

    def get_input():
        nums_in = [map(int, input().split()[1:]) for i in range(K)]
        return nums_in

    def get_product(nums_in):
        combinations = list(set(product(*nums_in)))
        get_max = (sum(i*i for i in combinations[0]) % M)
        return combinations, get_max

    def get_final(combinations, get_max):
        for j in range(1, len(combinations) - 1):
            temp_max = sum(k*k for k in combinations[j]) % M
            if temp_max > get_max:
                get_max = temp_max
        print(get_max)


    nums_in = get_input()
    combinations, get_max = get_product(nums_in)
    get_final(combinations, get_max)

solver(K, M)

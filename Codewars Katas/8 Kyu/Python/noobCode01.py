'''

Codewars Kata - 8 Kyu - noobCode 01: SUPERSIZE ME.... or rather, this integer!

Description:

Write a function that rearranges an integer into its largest possible value.

super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.


'''

def super_size(n):
    num_list = sorted([int(x) for x in list(str(n))], reverse=True)
    return(int(''.join(map(str, num_list))))
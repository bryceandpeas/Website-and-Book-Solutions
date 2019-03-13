'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 1: Standard Deviation

Objective
In this challenge, we practice calculating standard deviation.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of  decimal place
(i.e., format). An error margin of  will be tolerated for the standard deviation.

'''

n = int(input().strip())
x = [int(i) for i in input().strip().sn = int(input())
nums = sorted([int(num) for num in input().split()])

def median(nums):
    if (len(nums) % 2) == 0:
        return int(sum(nums[len(nums) // 2-1:len(nums) // 2+1]) / 2)
    else:
        return nums[len(nums) // 2]

def quartiles(n, nums):
    q1 = median(nums[:len(nums) // 2])
    q2 = median(nums)
    if (n % 2)  == 0:
        q3 = median(nums[len(nums) // 2:])
    else:
        q3 = median(nums[len(nums) // 2+1:])
    return (q1, q2, q3)

q1, q2, q3 = quartiles(n, nums)
print('{0}{3}{1}{3}{2}'.format(q1, q2, q3, '\n'))
plit()]

m = (sum(x) / n)
v = (sum(((i - m) ** 2) for i in x) / n)
sdev = (v ** 0.5)

print("{0:0.1f}".format(sdev))

'''

Hackerank Domains: https://www.hackerrank.com/domains

Tutorials https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

Hackerrank - 10 Days Of Statistics - Day 4: Binomial Distribution I

Objective
In this challenge, we learn about binomial distributions.
Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is .
If there is  child born per birth, what proportion of Russian families
with exactly  children will have at least  boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of  decimal places (i.e.,  format).



'''

b, g = [float(x) for x in input().split()]

def fac(n):
    return 1 if n < 2 else n * fac(n - 1)

def k_choices(n, k):
    return fac(n) / (fac(k) * fac(n - k))

def odds(target, other):
    return (target/(target+other), other/(target+other))

def min_k(n, k):
    total_odds = 0
    while k <= n:
        combs = k_choices(n, k)
        total_odds += combs * odds(b, g)[0] ** k * odds(b, g)[1] ** (n - k)
        k += 1
    return total_odds

out = min_k(6,3)

print('{:0.3f}'.format(out))

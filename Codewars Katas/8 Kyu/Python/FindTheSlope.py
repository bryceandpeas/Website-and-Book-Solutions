'''

Codewars Kata - 8 Kyu - Find the Slope

Description:

Given an array of 4 integers
[a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.

For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.

Assume that [a,b,c,d] and the answer are all integers (no floating numbers!). Slope: https://en.wikipedia.org/wiki/Slope

'''

def find_slope(points):
    x = points[0]
    y = points[1]
    xx = points[2]
    yy = points[3]
    if x != 0 and xx != 0:
        if (x - xx) != 0:
            return (str(((y - yy) / (x - xx))))
        else:
            return ('undefined')

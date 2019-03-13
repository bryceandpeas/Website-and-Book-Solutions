'''

Codewars Kata - 8 Kyu - Beginner Series #4 Cockroach

Description:

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

cockroach_speed(1.08) == 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

'''

def cockroach_speed(s):
    return(int(s * 27.777777777778))
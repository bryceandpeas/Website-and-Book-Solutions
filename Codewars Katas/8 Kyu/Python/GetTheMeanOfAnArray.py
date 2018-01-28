'''

Codewars Kata - 8 Kyu - Get the mean of an array

Description:

It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded downward to its nearest integer.

The array will never be empty.

'''

def get_average(marks):
    average_add = 0
    average = 0
    for i in marks:
        average_add += i
        average = average_add / len(marks)
    return (average)


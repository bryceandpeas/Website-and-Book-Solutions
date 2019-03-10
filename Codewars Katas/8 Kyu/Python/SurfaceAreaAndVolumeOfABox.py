'''

Codewars Kata - 8 Kyu - Surface Area and Volume of a Box

Description:

Write a function that returns the total surface area and volume of a box as an array: [area, volume].

'''

def get_size(w,h,d):
    volume = (w * h * d)
    area = ((2 * (w * h)) + (2 * (d * h)) + (2 * (d * w)))
    return([area, volume])
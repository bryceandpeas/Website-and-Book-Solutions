'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Classes: https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

Hackerrank - Python -  Classes - Class 2 - Find the Torsional Angle

You are given four points  and  in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points  and  in degrees(not radians). Let the angle be . 

 where  x  and  x .

Here,  means the dot product of  and , and  x  means the cross product of vectors  and . Also, .

Input Format

One line of input containing the space separated floating number values of the  and  coordinates of a point.

Output Format

Output the angle correct up to two decimal places.

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2
Sample Output

8.19

'''



class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return (Points(self.x - no.x, self.y - no.y, self.z - no.z))

    def dot(self, no):
        return (self.x * no.x + self.y * no.y + self.z * no.z)

    def cross(self, no):
        return Points(self.y*no.z - self.z*no.y, self.z*no.x - self.x*no.z, self.x*no.y - self.y*no.x)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)



'''
5 Crucial Projects for Beginners - https://www.daniweb.com/programming/software-development/threads/131973/5-crucial-projects-for-beginners

3 - Area Calculator:

Overview:

The user will be prompted with a menu where he/she will select a shape.
Then the user will give the appropriate information needed to solve for the area,
and the computer will give the area! Hope you all have taken geometry!
What you will be Using:
Input/Output, Integers, Variables, Strings, Print, If/Elif/Else
My Thoughts on Project:
Great if you understand geometry and want to write a program that will do a little homework for you!
This program is great for learning variables and creation of math related projects.
'''

import math

def menu():
  print(' ---------------------\n',
      '|       Menu        |\n',
      '---------------------\n',
      '| 0 | Square        |\n',
      '| 0 | Rectangle     |\n',
      '| 0 | Parallelogram |\n',
      '---------------------\n',
      '| 1 | Circle        |\n',
      '---------------------\n',
      '| 2 | Triangle      |\n',
      '---------------------\n')

# Shape functions

def square(square_width, square_height):
  area = (square_width * square_height)
  return(area)

def circle(circle_radius):
  area = (math.pi * (circle_radius^2))
  return(area)

def triangle(triangle_width, triangle_height):
  area = ((triangle_width * triangle_height) / 2)
  return(area)

def main():

  menu()

  try:
    shape_selection = int(input('Please select your shape: '))

  except:
    print('You must select your shape via its assigned number\n',
        'Restarting...')
    main()

  try:
    if shape_selection == 0:
      print('You have selected square, rectangle or parallelogram.\n')
      square_width = (int(input('\nPlease enter the width: ')))
      square_height = (int(input('\nPlease enter the height: ')))

      area = square(square_width, square_height)

    elif shape_selection == 1:
      print('You have selected circle.\n')
      circle_radius = (int(input('\nPlease enter the radius: ')))

      area = circle(circle_radius)

    elif shape_selection == 2:
      print('You have selected triangle.\n')
      triangle_width = (int(input('\nPlease enter the width: ')))
      triangle_height = (int(input('\nPlease enter the height: ')))

      area = triangle(triangle_width, triangle_height)

    final_area = '\nYour shape\'s area is: {0}units^2\n'.format(area)

    print(final_area)

  except:
    print('You must ensure your input only consists of numbers.')
    main()

if __name__ == '__main__':
  main()

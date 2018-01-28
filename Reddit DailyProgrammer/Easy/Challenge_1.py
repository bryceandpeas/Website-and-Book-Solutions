'''

Reddit Daily Programmer - /r/dailyprogrammer

[Easy] - Challenge #1

create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.

'''

name = input('Please enter your name: ')
age = input('Please enter your age: ')
username = input('Please enter your reddit username: ')

with open('Reddit_DailyProgrammer_Challenge1.txt', 'w') as output_file:
	output_file.write(name)
	output_file.write(age)
	output_file.write(username)

output_file.close()


print('Your name is {0}, you are {1} years old and your reddit username is {2}.'.format(name, age, username))

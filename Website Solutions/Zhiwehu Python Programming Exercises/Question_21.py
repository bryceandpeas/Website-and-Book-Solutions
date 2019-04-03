'''

Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def get_steps():
	print("Please enter your robots moves in the format \"DIRECTION STEPS\" where \"DIRECTION\" is Up, Down, Left or Right and \"STEPS\" is a number." + "\n")

	step_amount = int(input("How many directions would you like to enter?: "))

	print("\n")

	steps = []
	for i in range(step_amount):
	    steps.append(tuple((input("Please enter direction {0}: ".format(i + 1))).split(' ')))

	return steps

def calc_distance(steps):
	horizontal = 0
	vertical = 0
	output_distance = [horizontal, vertical]

	for i in steps:
		if i[0].upper() == "UP":
			vertical += int(i[1])
		elif i[0].upper() == "DOWN":
			vertical -= int(i[1])
		if i[0].upper() == "LEFT":
			horizontal -= int(i[1])
		elif i[0].upper() == "RIIGHT":
			horizontal += int(i[1])
		else:
			continue

	output_distance = [horizontal, vertical]

	return output_distance

steps = get_steps()

print(max(calc_distance(steps)))
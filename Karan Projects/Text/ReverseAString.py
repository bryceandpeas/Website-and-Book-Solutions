'''

Karan 100 Projects - Text - Reverse a String

Enter a string and the program will reverse it and print it out.

'''

user_string = input('Please enter a string to reverse: ')

string_list = []

for i in user_string:
	string_list.append(i)

output_string = ''.join(string_list[::-1])

print(output_string)

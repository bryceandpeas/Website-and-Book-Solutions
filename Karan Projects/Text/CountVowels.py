'''	

Karan 100 Projects - Text - Count Vowels

Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.

'''

user_string = input('Please enter a string to count vowels in: ')

vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_sums = {}
total_vowels = 0

for i in user_string:
	if i in vowel_list:
		if i in vowel_sums:
			vowel_sums[i] = vowel_sums[i] + 1
			total_vowels += 1
		else:
			vowel_sums[i] = 1
			total_vowels += 1

print ('\n' + 'There are ' + str(total_vowels) + ' vowels in your string.' + '\n')
print('There are: ' + '\n')
for vowel, vowel_sum in vowel_sums.items():
	print(str(vowel_sum) + ' ' + str(vowel) + '\'s')

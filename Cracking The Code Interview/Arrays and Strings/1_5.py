'''

Implement a method to perform basic string compression using the counts of repeated amtacters. 
For example, the string aabcccccaaa would become a2b1c5a3. 
If the "compressed" string would not become smaller than the orig- inal string, 
your method should return the original string.

'''

from itertools import groupby

def string_compressor(string):
	temp = list((''.join(c + str(len(list(amt)))) for c, amt in groupby(string)))
	if (sum(1 for _ in temp)) > len(string):
		print(string)
	else:
		for i in temp:
			print(i, end='')

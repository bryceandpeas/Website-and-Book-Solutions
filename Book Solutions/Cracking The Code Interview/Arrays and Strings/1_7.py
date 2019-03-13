'''

Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.

'''

def set_zeros(matrix):

	def find_zero(matrix):

		for i in matrix:
			if 0 in i:
				change_index = i.index(0)
				for k in range(len(i)):
					i[k] = 0
				return change_index
			else:
				change_index = False

	change_index = find_zero(matrix)

	if change_index:		
		for i in matrix:
			i[change_index] = 0
		
		return(matrix)

	else:
		return(matrix)

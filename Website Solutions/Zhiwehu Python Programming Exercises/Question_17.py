'''

Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def get_transactions():
	print("Please enter your transaction amount in the format \"X NNN\"." + "\n"
		  + "Where X is D or W for Deposit or withdrawal and N is an amount of any length." + "\n")

	line_amount = int(input("How many lines of transactions would you like to enter?: "))

	print("\n")

	transactions = []
	for i in range(line_amount):
	    transactions.append((input("Please enter line {0}: ".format(i + 1))).replace(' ', ''))

	return transactions

def calulate_transactions(transactions):
	output_amount = 0
	for i in transactions:
		if i[:1] == "D":
			output_amount += int(i[1:])
		elif i[:1] == "W":
			output_amount -= int(i[1:])
		else:
			print("Inacurate transaction")
			continue

	return output_amount

transactions = get_transactions()

print(calulate_transactions(transactions))
from GoCardAccount import *

def printBalance():
	balance = newAccount.getBalance()
	print('Balance = ${:.2f}'.format(balance))



initialBalance = None
while initialBalance == None:
	try:
		initialBalance = float(input('Creating account. Input initial balance: '))
		newAccount = GoCardAccount(initialBalance)
	except ValueError:
		print('\nPlease enter a valid number.\n')
		initialBalance = None

functions = {

	'r': newAccount.takeRide,
	't': newAccount.topUp,
	'b': printBalance,
	'q': newAccount.printStatementQuit

}

while True:
	userInput = input('? ').split()

	try:
		if len(userInput) == 0:
			pass

		elif len(userInput) == 1:
			function = userInput[0]
			functions[function]()

		elif len(userInput) == 2:
			function = userInput[0]
			parameter = float(userInput[1])
			functions[function](parameter)

		else:
			print('Bad command.')

	except (KeyError, TypeError, ValueError):
		print('Bad command.')

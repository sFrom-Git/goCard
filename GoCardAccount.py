class GoCardAccount:

	"""
	Go-Card Account module for Python
	=================================

	The class GoCardAccount must be passed an integer or float value
	when it is instantiated. This will be the initial balance on the account.
	"""

	def __init__(self, initialBalance):
		self._statementLog = []
		self._currentBalance = initialBalance
		self._statementLog.append(initialBalance)

	def takeRide(self, cost):
		"""Must be passed an integer or float, deducts that amount from the current
		   balance if the amount is greater than 0. 
		   Records the amount in a list of transactions"""
		if cost > 0:
			self._currentBalance -= cost
			self._statementLog.append(-cost)
		else:
			print('Please enter a value greater than 0')

	def topUp(self, amount):
		"""Must be passed an integer or float, adds that amount to the current
		   balance if the amount is greater than 0. 
		   Records the amount in a list of transactions"""
		if amount > 0:
			self._currentBalance += amount
			self._statementLog.append(amount)
		else:
			print('Please enter a value greater than 0')

	def getBalance(self):
		"""Returns the current balance as a float"""
		return float(self._currentBalance)

	def printStatementQuit(self):
		"""Prints the list of transactions with some formatting for readability.
		   Then terminates the program"""
		self._initialBalance = self._statementLog.pop(0)

		print('{: <20} {: >10} {: >10}'.format('EVENT', 'AMOUNT ($)', 'BALANCE ($)'))
		print('{: <20} {: >10} {: >10.2f}'.format('Initial balance', '', self._initialBalance))

		self._printingBalance = self._initialBalance
		for i in range(len(self._statementLog)):
			
			if self._statementLog[i] < 0:
				self._event = 'Ride'
			else:
				self._event = 'Top up'

			self._printingBalance += self._statementLog[i]
			print('{: <20} {: >+10.2f} {: >10.2f}'.format(self._event, self._statementLog[i], self._printingBalance))

		print('{: <20} {: >10} {: >10.2f}'.format('Final balance', '', self._printingBalance))
		quit()

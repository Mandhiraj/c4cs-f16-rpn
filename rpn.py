import sys
from termcolor import colored
import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'&': operator.and_,
	'|': operator.or_,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		result_str = str(result)
		print("Result: ")
		if(result < 0):
			print(colored(result_str, 'red'))
		else:
			print(colored(result_str, 'green'))

if __name__ == '__main__':
	main()

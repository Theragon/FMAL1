import sys

class Interpreter:
	stack = []
	data = ''
	add = False
	mult = False
	prnt = False
	lines = []

#	def __init__(self):
#		print 'constructor'

	def start(self):
		print 'start'

		self.lines = sys.stdin.readlines()
		self.fetch()
	
	def fetch(self):
		print 'fetch'

		for line in self.lines:
			self.data = line
			self.decode()

	def decode(self):
		print 'decode'

		length = len(self.data)

		if length <= 1:
			sys.exit()

		if self.data.find('PUSH',0,4) == 0:
			value = self.data[5:length-1]
			value = int(value, base=10)
			self.stack.append(value)

		if self.data.find('ADD',0,3) == 0:
			self.add = True

		if self.data.find('MULT',0,4) == 0:
			self.mult = True

		if self.data.find('PRINT',0,5) == 0:
			self.prnt = True

		else:
			print 'Error for operator: nameOfOperator'

		self.execute()

	def execute(self):
		print 'execute'
		if self.add == True:
			a = self.stack.pop()
			b = self.stack.pop()
			result = a+b
			self.stack.append(result)
			self.add = False

		if self.mult == True:
			a = self.stack.pop()
			b = self.stack.pop()
			result = a*b
			self.stack.append(result)
			self.mult = False

		if self.prnt == True:
			print 'RESULT: ', self.stack[0]
			self.prnt = False

def main():
	intrpr = Interpreter()
	intrpr.start()

if __name__ == '__main__':
	main()
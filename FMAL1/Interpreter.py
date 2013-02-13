import sys

class Interpreter:
	stack = []
	data = ''
	add = False
	mult = False
	prnt = False

	def start(self):

		self.lines = sys.stdin.readlines()
		self.fetch()
	
	def fetch(self):

		for line in self.lines:
			self.data = line
			self.decode()

	def decode(self):

		length = len(self.data)

		if length <= 1:
			sys.exit()

		elif self.data.find('PUSH',0,4) == 0:
			if length<=6:
				print 'Interpreter error invalid instruction: PUSH'
				sys.exit()
			else:
				value = self.data[5:length-1]
				if value.isdigit():
					value = int(value, base=10)
					self.stack.append(value)
				else:
					print 'Interpreter error invalid instruction: PUSH'

		elif self.data.find('ADD',0,3) == 0:
			self.add = True

		elif self.data.find('MULT',0,4) == 0:
			self.mult = True

		elif self.data.find('PRINT',0,5) == 0:
			self.prnt = True

		else:
			print 'Error for operator'

		self.execute()

	def execute(self):
		if self.add == True:
			if len(self.stack)>1:
				a = self.stack.pop()
				b = self.stack.pop()
				result = a+b
				self.stack.append(result)
			else:
				print 'Interpreter error: Too few arguments for operator ADD'
			self.add = False

		if self.mult == True:
			if len(self.stack)>1:
				a = self.stack.pop()
				b = self.stack.pop()
				result = a*b
				self.stack.append(result)
			else:
				print 'Interpreter error: Too few arguments for operator MULT'
			self.mult = False

		if self.prnt == True:
			if len(self.stack)>0:
				print self.stack[0]
			else:
				print 'Interpreter error'

			self.prnt = False

def main():
	intrpr = Interpreter()
	intrpr.start()

if __name__ == '__main__':
	main()
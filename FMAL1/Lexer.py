import string
from Token import *
#from Parser import *

class Lexer:

		
	def __init__(self):
		self.text = raw_input('type something: ')
		self.count = 0

	def nextToken(self):
		token = Token()
		length = len(self.text)
		digitlist = ''

		print 'nextToken'

#		x = count
		if self.count == length:
				self.count +=1
				return "END", 'END'
			
		for x in range(self.count, length):		
			self.count = x
			if self.text[x].isspace():
				continue
			print 'X: ', x
			if self.text[x] == '(':
				self.count +=1	
				return '(', 'LPAREN'
			if self.text[x] == ')':
				self.count +=1
				return ')', 'RPAREN'
			if self.text[x] == '+':
				self.count +=1
				return '+', 'PLUS' 		
			if self.text[x] == '*':
				self.count +=1
				return '*', 'MULT'	

			if self.text[x].isdigit():
				while self.text[x].isdigit():
					digitlist += self.text[x]
					if len(digitlist)>0 and x < length-1:
						print "spam"
						x = x + 1
					else:
						self.count = self.count + len(digitlist)
						return int(digitlist, base=10), 'INT'	
				self.count = self.count + len(digitlist)																					
				return int(digitlist, base=10), 'INT'
			else:
				self.count +=1
				return 'ERR', 'ERR'

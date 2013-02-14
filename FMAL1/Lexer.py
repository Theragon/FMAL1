import string
from Token import *
#from Parser import *

class Lexer:

		
	def __init__(self):
		self.text = raw_input()
		self.count = 0

	def nextToken(self):
		token = Token('2')
		length = len(self.text)
		digitlist = ''

		if self.count == length:
				self.count +=1
				return Token('END')
			
		for x in range(self.count, length):		
			self.count = x
			if self.text[x].isspace():
				continue
			if self.text[x] == '(':
				self.count +=1	
				return Token(self.text[x])
			if self.text[x] == ')':
				self.count +=1
				return Token(self.text[x])
			if self.text[x] == '+':
				self.count +=1
				return Token(self.text[x]) 		
			if self.text[x] == '*':
				self.count +=1
				return Token(self.text[x])	

			if self.text[x].isdigit():
				while self.text[x].isdigit():
					digitlist += self.text[x]
					if len(digitlist)>0 and x < length-1:
						x = x + 1
					else:
						self.count = self.count + len(digitlist)
						#token = Token 
						return Token(int(digitlist, base=10))	
				self.count = self.count + len(digitlist)																					
				return Token(int(digitlist, base=10))
			else:
				self.count +=1
				return token("ERR")

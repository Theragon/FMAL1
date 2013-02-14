from Lexer import *

class Token():
	lexeme = ""
	tCode = ""

	def __init__(self, value):
		self.lexeme = value
					
		if value == '+':
			self.tCode = "PLUS"
		elif value == '*':
			self.tCode = "MULT"
		elif value == '(':
			self.tCode = "LPAREN"
		elif value == ')':
			self.tCode = "RPAREN"
		elif value == 'ERROR':
			self.tCode = "ERROR"
		elif value == 'END':
			self.tCode = "END"
		else: 
			self.tCode = "INT"	


from Token import *
from Lexer import *
import sys

class Parser:
	text = ''
	value = 0
	code = 0
	token = ""

	def parse(self):
		lexer = Lexer()
		self.token = lexer.nextToken()
		self.expr(lexer)
		print 'PRINT'

		if lexer.count < len(lexer.text)+1:
			print 'Syntax error!'

	def expr(self, lexer):	
		self.term(lexer)	
		
		while self.token.tCode == 'PLUS':
			self.token = lexer.nextToken()
			self.expr(lexer)
			print 'ADD'

	def term(self, lexer):
		self.factor(lexer)
		
		#print "Tokencode : ", self.token.tCode
		while self.token.tCode == 'MULT':	
			self.token = lexer.nextToken()
			self.term(lexer)
			print 'MULT'

	def factor(self, lexer):
		

		if self.token.tCode == 'INT':
			value = str(self.token.lexeme)
			pushint = 'PUSH '
			pushint += value 
			print pushint
			self.token = lexer.nextToken()
			
		elif self.token.tCode == 'LPAREN':
			self.token = lexer.nextToken()
			
			self.expr(lexer)
			if self.token.tCode == 'RPAREN':
				self.token = lexer.nextToken()
			else:
				self.error()
		else:
			self.error()

	def error(self):
		print 'Syntax error!'
		sys.exit()

#test
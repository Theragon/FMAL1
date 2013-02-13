from Token import *
from Lexer import *
import sys

class Parser:
	text = ''
	value = 0
	code = 0

	def parse(self):
		print 'parse'
		token = Token()
		lexer = Lexer()

		self.value, self.code = lexer.nextToken()
		self.expr(lexer)
		print "PRINT"

	def expr(self, lexer):	
		self.term(lexer)	
		
		while self.code == 'PLUS':
			self.value, self.code = lexer.nextToken()
			self.expr(lexer)
			print "ADD"

	def term(self, lexer):
		self.factor(lexer)
		
		while self.code == 'MULT':	
			self.value, self.code = lexer.nextToken()
			self.term(lexer)
			print "MULT"

	def factor(self, lexer):
		
		if self.code == 'INT':
			value = str(self.value)
			pushint = "PUSH "
			pushint += value 
			print pushint
			self.value, self.code = lexer.nextToken()
			
		elif self.code == 'LPAREN':
			self.value, self.code = lexer.nextToken()
			
			self.expr(lexer)
			if self.code == 'RPAREN':
				self.value, self.code = lexer.nextToken()
			else:
				self.error()
		else:
			self.error()

	def error(self):
		print 'ERRRORROROROROROR'
		sys.exit()
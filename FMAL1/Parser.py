from Token import *
from Lexer import *

class Parser:
	stack = []
	text = ''
	value = 0
	code = 0
#	count = 0

	def parse(self):
		print 'parse'
		token = Token()
		lexer = Lexer()

		self.value, self.code = lexer.nextToken()
		self.expr(lexer)

	
	def expr(self, lexer):
		print 'inni expr'
		self.term(lexer)
		print  'value', self.value, 'tala', self.code
		while self.code == 'PLUS':
			self.value, self.code = lexer.nextToken()
			self.expr(lexer)

	def term(self, lexer):
		print 'inni term'
		self.factor(lexer)
		while self.code == 'MULT':
			self.value, self.code = lexer.nextToken()
			self.term(lexer)

	def factor(self, lexer):
		print 'inni factor'
		if self.code == 'INT':
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
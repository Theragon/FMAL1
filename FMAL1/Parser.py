from Token import *
from Lexer import *

class Parser:
	stack = []
	text = ''
#	count = 0

	def parse(self):
		print 'parse'
		token = Token()
		#lexer = Lexer()
		#text = raw_input('type something: ')

#		Parser.getLex(self, lexer, text)
		Parser.expr(self)

	
	def expr(self):
		count = 0
		lexer = Lexer()
		value, code = lexer.nextToken()
		print  'value', value, 'tala', code 

		value, code1 = lexer.nextToken()
		print 'value', value, 'tala ', code1 

		value, code2 = lexer.nextToken()
		print 'value', value, 'tala ', code2 

	#def term(self, )	
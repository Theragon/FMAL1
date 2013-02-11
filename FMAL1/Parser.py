from Token import *
from Lexer import *

class Parser:
	stack = []
	text = ''
#	count = 0

	def parse(self):
		print 'parse'
		token = Token()
		lexer = Lexer()
		text = raw_input('type something: ')

#		Parser.getLex(self, lexer, text)
		Parser.expr(self, text)


	def intFunc(self, lexer, param, text):
		Parser.stack.append(param)
		print 'intfunc'
		print Parser.stack 
		Parser.getLex(self, lexer, text)

	def lParenFunc(self, lexer, param, text):
		Parser.stack.append(param)
		print 'lParenFunc'
		print Parser.stack
		Parser.getLex(self, lexer, text)

	def rParenFunc(self, lexer, param, text):
		Parser.stack.append(param)
		print 'rParenFunc'

	def getLex(self, lexer, param):
		text = param
		token = Token()
		nextLex = lexer.nextToken(text)
		if nextLex == token.tcode.ONE:
			Parser.intFunc(self, lexer, token.tcode.ONE, text)
		if nextLex == token.tcode.FOUR:
			Parser.lParenFunc(self, lexer, token.tcode.FOUR, text)
		if nextLex == token.tcode.FIVE:
			Parser.rParenFunc(self, lexer, token.tcode.FIVE, text)
	
	def expr(self, text):
		count = 0
		lexer = Lexer()
		code1, count = lexer.nextToken(text, count)
		print 'tala ', code1, ' count ', count

		code2, count = lexer.nextToken(text, count)
		print 'tala ', code1+code2, ' count ', count
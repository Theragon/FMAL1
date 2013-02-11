import string
from Token import *
#from Parser import *

class Lexer:
#	def __init__(self, param):

	def nextToken(self, text):
		token = Token()
		lex = text

		length = len(lex)
#		length2 = len(Parser.text)

		for x in xrange(0,length):
			if lex[x].isdigit():
				print x+1
				return token.tcode.ONE, x
			if lex[x] == '(':
				print 'token code FOUR returned'
				return token.tcode.FOUR
			if lex[x] == ')':
				print 'token code FIVE returned'
				return token.tcode.FIVE
			if lex[x] == '+':
				return token.tcode.TWO
			if lex[x] == '*':
				return token.tcode.THREE
			if lex[x] == '\n':
				return token.tcode.SEVEN
			else:
				return token.tcode.SIX

	def nextTokenTest(self, text, count):
		token = Token()
		text = text
		length = len(text)

		x = count

		for x in range(count, length):
			count = x
			if text[x] == '(':
				print 'found: (', x
				return token.tcode.FOUR, count
			if text[x] == ')':
				return 
			if text[x].isdigit():
				return text[x]

#		print 'count: ', x+1

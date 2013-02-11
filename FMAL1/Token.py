from Lexer import *

class Token:
	lexeme = ''
	def TokenCode(**enums):
		return type('Enum', (), enums)

	tcode = TokenCode(ONE='INT', TWO='PLUS', THREE='MULT', FOUR='LPAREN', FIVE='RPAREN', SIX='ERROR', SEVEN='END')

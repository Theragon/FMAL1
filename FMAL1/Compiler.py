from Lexer import *
from Token import *
from Parser import *
from Interpreter import *

class Compiler:
	parser = Parser()
	parser.parse()
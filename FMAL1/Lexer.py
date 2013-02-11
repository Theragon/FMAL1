import string
from Token import *
#from Parser import *

class Lexer:
#	def __init__(self, param):


	def nextToken(self, text, count):
		token = Token()
		length = len(text)
		digitlist = ''

		print 'nextToken'

#		x = count

		for x in range(count, length):
			#count += 1
			print 'X: ', x
			if text[x] == '(':
				print 'found: (', x
				count = x
				return '(', count
			if text[x] == ')':
				return 
			if text[x].isdigit():
				while text[x].isdigit():
					print 'inni i luppu', x
					digitlist += text[x]
					if x<=length-1:
						x+=1
						print 'x inn i if ', x
					count = x
				
				print 'return digitlist'
				return int(digitlist, base=10), count
			if text[x].isspace():
				pass

#		print 'count: ', x+1

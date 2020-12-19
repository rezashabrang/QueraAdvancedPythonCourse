import re

try:
	while True:
		line = input()
		pattern = r'^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$'
		if re.match(pattern, line):
			print('LEGAL')
		else:
			print('ILLEGAL')
except:
	pass
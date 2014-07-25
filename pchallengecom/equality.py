#http://www.pythonchallenge.com/pc/def/equality.html
#http://www.pythonchallenge.com/pc/def/linkedlist.php
#http://wiki.pythonchallenge.com/index.php?title=Main_Page
#http://wiki.pythonchallenge.com/index.php?title=Level3:Main_Page

import string
import re

def main():
	""" 
	This is testing for comments
	for multiple lines
	f = open('somefile.txt','r')
	for line in f.readlines():
    	print line
	f.close()

	"""
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	result = []

	fo = open('equality','r')
	txt = fo.read()
	res = re.findall(r'([a-z][A-Z]{3})([a-z])([A-Z]{3}[a-z])',txt)
	#print res
	for ch in res:
		result.append(ch[1])
	print ''.join(result) 

	"""

	l = len(txt)-4
	for i in range (4, l):
		if txt[i] in lower:
			if txt[i-3] in upper and txt[i-2] in upper and txt[i-1] in upper and txt[i+1] in upper and txt[i+2] in upper and txt[i+3] in upper:
				if txt[i-4] in lower and txt[i+4] in lower:
					result.append(txt[i])

	print ''.join(result)
	"""

if __name__=='__main__':
	main()





	
#http://www.pythonchallenge.com/pc/def/ocr.html
#http://www.pythonchallenge.com/pc/def/equality.html
#http://www.pythonchallenge.com/pcc/def/equality.html 

#
#
from operator import itemgetter 
def main():
	dit = {}
	l = []
	fo = open("ocrinput", 'r')
	text = fo.read()
	for char in text:
		if char in dit.keys():
			dit[char] = dit[char]+1
		else:
			dit[char] = 1
			l.append(char)
	#result = sorted(dit.items(), key = itemgetter(1))
	#print result
	print l


if __name__ =='__main__':
	main()

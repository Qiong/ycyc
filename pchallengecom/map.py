<<<<<<< HEAD
#http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page

=======
>>>>>>> e84bc415595febd40acfbb134b5b2a0473b0c8ff
import string
from string import maketrans

result = []
def main():
	#char = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	char = "map"
	for ch in char:
		if ch == 'y':
			result.append('a')
		elif ch == 'z':
			result.append('b')
		elif ch in string.lowercase:
			#print 2+ ord(ch)
			result.append (chr(2+ ord(ch)))
		else:
			result.append (ch)
def maketranss():
	intab = 'abcdefghijklmnopqrstuvwxyz'
	outtab ='cdefghijklmnopqrstuvwxyzab'
	#char = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	char = "http://www.pythonchallenge.com/pc/def/map.html"
	print char.translate(maketrans(intab,outtab))
	

if __name__ =="__main__":
	main()
	maketranss()
	print ''.join(result)

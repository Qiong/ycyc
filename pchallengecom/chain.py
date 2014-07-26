#follow the link
#http://www.pythonchallenge.com/pc/def/linkedlist.php
#  http://www.pythonchallenge.com/pc/def/peak.html
#http://wiki.pythonchallenge.com/index.php?title=Level4:Main_Page
"""
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->
<center>
<a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>
A possibly clearer way uses a list comprehension instead of map():
>>> for linelist in banner:
...     line = [ch * count for ch, count in linelist]
...     print "".join(line)
"""
import urllib2
import re
import time
def main():
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
	p1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
	number =12345
	response = ""
	n=1
	while (n<=400):
		response = urllib2.urlopen(url)
		txt = response.read()
		#print txt
		#time.sleep(1)
		match = re.search(r'(and the next nothing is )(.*)',txt)
		#print match.group()
		if match:
			number = match.group(2)
			print number
			url = p1 + number
			n +=1
		else:
			print 'last number is ', number
			url = p1 + str(int(number)/2)
			n +=1
	print 'the final url is ' , url


if __name__ == '__main__':
	main()


###http://www.pythonchallenge.com/pc/def/hockey.html
#
#http://www.pythonchallenge.com/pc/def/integrity.html
#http://www.pythonchallenge.com/pcc/def/integrity.html
#
from PIL import Image

import StringIO
import zipfile
import urllib2
import re

def get_challenge(str):
	prefix= 'http://www.pythonchallenge.com/pc/'
	return urllib2.urlopen(prefix+str).read()

def get_image(s):
	return Image.open(StringIO.StringIO(get_challenge(s)))


def main():
	im = get_image('def/oxygen.png')
	#print im.size
	w,h = im.size
	#print im.getpixel((0, h/2))
	#print ''.join(chr(im.getpixel((i,h/2))[0])   for i in range (0,w,7))
	print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))




if __name__ == '__main__':
	main()

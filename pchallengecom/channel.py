#http://www.pythonchallenge.com/pc/def/channel.html
#http://www.pythonchallenge.com/pcc/def/oxygen.html

#http://www.pythonchallenge.com/pc/def/oxygen.html
#
#
import StringIO
import zipfile
import urllib2
import re

def get_challenge(str):
	prefix= 'http://www.pythonchallenge.com/pc/'
	return urllib2.urlopen(prefix+str).read()

def next(p,zip):
	#z=zipfile.ZipFile(StringIO.StringIO(get_challenge('def/channel.zip')))
	z=zip
	txt = z.read('%s.txt' % p)
	m = re.match('Next nothing is ([0-9]+)',txt)
	if not m: 
		print txt
		return
	return m.group(1)
def main():
	z=zipfile.ZipFile(StringIO.StringIO(get_challenge('def/channel.zip')))
	#print z.namelist()
	#print z.read('readme.txt')
	#print z.read('90052.txt')
	zpp=[]
	p=90052
	
	while next(p,z):
		zpp.append(p)
		p=next(p,z)

	#print p
	print ''.join([z.getinfo('%s.txt' %p).comment  for p in zpp  ])


"""
	for i in range(len(z.namelist())):
		zpp.append(p)
		if next(p,z):
			p=next(p,z)
		else: break
		#print p
	print ''.join([z.getinfo('%s.txt' %p).comment  for p in zpp  ])
	#print 'zpp is',zpp
"""	



if __name__=='__main__':
	main()

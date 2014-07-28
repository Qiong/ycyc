#http://www.pythonchallenge.com/pc/def/integrity.html
#
#http://www.pythonchallenge.com/pcc/return/good.html
#
#
import bz2

def get_challenge(str):
	prefix= 'http://www.pythonchallenge.com/pc/'
	return urllib2.urlopen(prefix+str).read()



def main():
	un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

	u = bz2.BZ2Decompressor().decompress(un)
	p = bz2.BZ2Decompressor().decompress(pw)
	print u,p



if __name__=='__main__':
	main()

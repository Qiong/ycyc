# http://www.pythonchallenge.com/pc/def/peak.html
#http://www.pythonchallenge.com/pcc/def/channel.html
#http://www.pythonchallenge.com/pc/def/channel.html

import pickle
import urllib2

def main():
	response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
	txt = response.read()
	result = pickle.loads(txt)
	#print result

	for code in result:
		temp =[]
		for item in code:
			temp.append(item[0]*item[1])
		print ''.join(temp)


if __name__=="__main__":
	main()
#!/usr/bin/python

import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://www.amazon.com"

urls = [url] # stack of urls to scrape
visited = [url] # hisotric record of urls

while len(urls) > 0 :
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0],'error spotted'

	soup = BeautifulSoup (htmltext)
	#print soup

	urls.pop(0)
	print len(urls)

	#print soup.findAll('a', href=True)
	for tag in soup.findAll('a', href=True) :
		tag['href'] = urlparse.urljoin(url, tag['href'])
		#print tag['href']
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

print visited

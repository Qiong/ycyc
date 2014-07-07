from scrapy.spider import Spider
from scrapy.selector import Selector
from test1.items import Test1Item
#from scrapy.http import Request

class test11(Spider):
	name = 'test11'
	allowed_domain = ["tutsplus.com"]
	start_url = ["http://code.tutsplus.com"]

	def parse(self, response):
		#open('aws.html', 'wb').write(response.body)
		hxs = Selector(response)
		titles = hxs.select('//[@class="posts__post-title"]/a/text()').extract()
		for title in titles:
			item = Test1Item()
			item["title"] = title
			yield item


 
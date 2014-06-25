from scrapy.spider import spider

class DmozSpider(Spider):
	name = "dmoz"
	allowed_domains = [".com"]
	start_urls = ["http://www.google.com"]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		open(filename, 'wb').write(response.body)
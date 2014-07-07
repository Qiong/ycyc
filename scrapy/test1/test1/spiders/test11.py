from scrapy.spider import Spider
from scrapy.selector import Selector
from test1.items import CraigslistSampleItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/", 
    			"http://seattle.craigslist.org/ctd/"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.select("//span[@class='pl']")
        items=[]
        for title in titles:
        	item = CraigslistSampleItem()
        	item["title"] = title.select("a/text()").extract()
        	item["link"] = title.select("a/@href").extract()
        	items.append(item)
    	return items
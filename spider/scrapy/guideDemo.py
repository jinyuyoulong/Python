import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class TorrentItem(scrapy.Item):
	"""docstring for TorrentItem"""
	def __init__(self, arg):
		super(TorrentItem, self).__init__()
		self.arg = arg

	url = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	size = scrapy.Field()

class xiaoshuoSpider(CrawlSpider):
	"""docstring for xiaoshuoSpider"""
	def __init__(self, arg):
		super(xiaoshuoSpider, self).__init__()
		self.arg = arg

	name = '530p'
	allowed_domains = ['www.530p.com']
	start_urls = ['http://www.530p.com/']
	rules = [Rule(LinkExtractor(allow=['/wuxia/']),'parse_torrent')]

	def parse_torrent(self, response):
		torrent = TorrentItem()
		torrent['url'] = response.url
		torrent['name'] = response.xpath("//div[@class='conter']/ul/li[1]/text()").extract()
		torrent['description'] = response.xpath("//div[@class='conter']/ul/li[2]/text()").extract()
		torrent['size'] = response.xpath("//div[@class='conter']/ul/li[4]/text()").extract()
		return torrent
		
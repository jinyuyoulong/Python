import scrapy

class m530pSpider(scrapy.Spider):
	name = "m530p"
	allowed_domins = ['www.530p.com']
	start_urls = [
		"http://www.530p.com/wuxia/",
		"http://www.530p.com/"
	]

    # 定义解析函数
	def parse(self, response):

        # urls = response.xpath('//div[@class="box"]/a/@href').extract()
		urls = response.xpath('//ul/li[@class="conter1"]/a/@href').extract()
        # for url in urls:
        #     yield Request(url, callback=self.parse_url)

		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(urls)




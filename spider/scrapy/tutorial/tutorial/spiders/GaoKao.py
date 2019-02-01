# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
import json

from items import MyspiderItem

class GaokaoSpider(scrapy.Spider):
    name = 'GaoKao'
    allowed_domains = ['www.gaokaopai.com']
    # start_urls = ['http://www.gaokaopai.com/rank-index.html']
    start_url = 'http://www.gaokaopai.com/rank-index.html'

    def __init__(self):
    	self.headers = {
    	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    	"X-Requested-With": "XMLHttpRequest"
    	}
    # 重写start_requests() 方法
    def start_requests(self):
    	for page in range(0,7):
    		formData = {
    		"otype": "4",
    		"city":"",
    		"start":str(25*page),
    		"amount":"25"
    		}

    		request = FormRequest(self.start_url, headers = self.headers,formdata = formData,callback=self.parse)
    		yield request

    def parse(self, response):
        # print(response.body)
        # print(response.url)
        content_type = response.headers["Content-Type"].decode('utf-8')
        # print(type(content_type))
        if (content_type.find("text/html")>0):
        	# print(response.body)
        	trs = response.xpath("//table[@id='results']//tr")[1:]
        	for item in trs:
        		school = MyspiderItem()
        		rank = item.xpath("td[1]/span/text()").extract()[0]
        		uni_name = item.xpath("td[2]/a/text()").extract()[0]
        		safehard = item.xpath("td[3]/text()").extract()[0]
        		city_code = item.xpath("td[4]/text()").extract()[0]
        		uni_type = item.xpath("td[6]/text()").extract()[0]

        		school['uni_name'] = uni_name
        		school["uni_id"] = ""
        		school["city_code"] = city_code
        		school['uni_type'] = uni_type
        		school["slogo"] = ""
        		school["rank"] = rank
        		school['safehard'] = safehard

        		yield school

        else:

        	data = json.loads(response.body_as_unicode())
        	# data = json.loads( response.body)# 也可以，但是不通用，只有当时utf-8 的时候才可以
        	print(data)
        	data = data["data"]["ranks"]#获取数据


        	for item in data:
        		school = MyspiderItem()
        		school["uni_name"] = item["uni_name"]
        		school["uni_id"] = item['uni_id']
        		school["city_code"] = item["city_code"]
        		school["uni_type"] = item["uni_type"]
        		school["slogo"] = item["slogo"]
        		school["rank"] = item["rank"]
        		school["safehard"] = item["safehard"]
				#将获取到的数据交给pipelines,pipelines在setting.py中定义
        		yield school

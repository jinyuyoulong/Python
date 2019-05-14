# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()

class MyspiderItem(scrapy.Item):
    uni_name = scrapy.Field()
    uni_id = scrapy.Field()
    city_code = scrapy.Field()
    uni_type = scrapy.Field()
    slogo = scrapy.Field()
    #录取难度
    safehard = scrapy.Field()
    rank = scrapy.Field()
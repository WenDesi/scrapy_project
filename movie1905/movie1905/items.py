# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class Movie1905Item(scrapy.Item):

    url = scrapy.Field()        # url
    html = scrapy.Field()       # 爬取下来的网页内容
    filename = scrapy.Field()   # 网页存储在本地的文件名

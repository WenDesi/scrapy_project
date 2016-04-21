import scrapy
import hashlib

from scrapy.selector import Selector
from movie1905.items import *

class Movie(scrapy.Spider):
    name = "chineseMovie"
    allowed_domains = ["1905.com"]

    def start_requests(self):
        basic_url = "http://www.1905.com/mdb/film/list/country-China/o0d0p%s.html"

        start,end = 0,485
        for i in range(start,end):
            url = basic_url.replace("%s",str(i))
            yield scrapy.http.Request(url,self.parse)

    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath('//ul[@class="inqList pt18"]/li/a/@href').extract()

        for url in urls:
            url = "http://www.1905.com" + url
            yield scrapy.http.Request(url,self.parse_movie)

    def parse_movie(self, response):
        item = Movie1905Item()
        item['url'] = response.url
        item['html'] = response.body
        item['filename'] = "movie_" + hashlib.sha1(response.url).hexdigest() + ".txt"

        print response.url
        return item


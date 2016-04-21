# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from SQLConnector import *
class Movie1905Pipeline(object):
    db = "movie"                                    # 数据库名
    filePath = "E://crawlerFile//movie//"       # 爬去下来的文件保存目录地址

    def __init__(self):
        self.SQLconn = SqlConnector(db=self.db)     # 我自己封装的数据库类

    def process_item(self, item, spider):
        self.save_in_File(item)
        self.save_in_DB(item)
        return item

    # 存入文件
    def save_in_File(self,item):
        file_object = open(self.filePath + item['filename'],'w')
        file_object.write(item['html'])
        file_object.close()

    # 存入数据库
    def save_in_DB(self,item):
        query = "insert into movie(url,filename) values(%s,%s)"
        query = self.SQLconn.generateQuery(query,[item['url'],item["filename"]])
        self.SQLconn.insert(query)
#encoding=utf-8

import pymysql

class SqlConnector(object):
    def __init__(self,host="localhost",port=3306,user="root",passwd="root",db="disease_ontology"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

        self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset = "utf8")

    def __del__(self):
        self.conn.close()

    def select(self,sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur._rows

    def insert(self,sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def update(self,sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def delete(self,sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def generateQuery(self,sql,paras):
        max_len = 2147483647
        query = sql
        for para in paras:
            para = para.replace("'",'')
            para = para.replace("%s",'')
            para = para.replace("%d",'')
            try:
                index_s = query.index("%s")
            except:
                index_s = max_len

            try:
                index_d = query.index("%d")
            except:
                index_d = max_len

            if index_d > index_s:
                query = query.replace("%s","'"+para+"'",1)
            else:
                query = query.replace("%d",str(para),1)

        return query

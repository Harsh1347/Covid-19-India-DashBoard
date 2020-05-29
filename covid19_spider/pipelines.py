# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class LearnPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('covid.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS cov """)
        self.curr.execute("""create table cov(
            index integer,
            state text,
            cnf_cases integer,
            cured integer,
            death integer
        )
        """)
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into cov values (?,?,?,?,?)""",(
            item['index'][0],
            item['state'][0],
            item['confirmed_cases'][0],
            item['cured'][0],
            item['death'][0]))
        self.conn.commit()
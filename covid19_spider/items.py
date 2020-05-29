# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnItem(scrapy.Item):
    index = scrapy.Field()
    state = scrapy.Field()
    confirmed_cases = scrapy.Field()
    cured = scrapy.Field()
    death = scrapy.Field()
    

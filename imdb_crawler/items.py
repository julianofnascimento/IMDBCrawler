# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    genre = scrapy.Field()
    actor = scrapy.Field()
    director = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
    pass
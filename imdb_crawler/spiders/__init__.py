# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from imdb_crawler.items import ImdbCrawlerItem
from bs4 import BeautifulSoup as bs
import json

class MySpider(CrawlSpider):
    name = 'imdb_crawler'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com']
    
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        html = bs(response.text)
        types = ["Movie", "TVSeries"]
        try:
            data_container = str(html.find(attrs={'type':'application/ld+json'}))
            page_data = json.loads(data_container)
            if page_data['@type'] in types:
                item = ImdbCrawlerItem()
                item['name'] = page_data['name']
                item['genre'] = page_data['genre']
                item['actor'] = [d['name'] for d in page_data['actor']]
                item['director'] = page_data['director']['name']
                item['description'] = page_data['description']
                item['date'] = page_data['datePublished']
                item['rating'] = page_data['aggregateRating']['ratingValue']
                return item
        except:
            pass
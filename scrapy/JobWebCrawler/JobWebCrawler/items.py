# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobwebcrawlerItem(scrapy.Item):

    # define the fields for your item here like:
    # name = Field()
    title = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    skills = scrapy.Field()

    summary = scrapy.Field()

    # source = scrapy.Field()
    found_date = scrapy.Field()
    source_url = scrapy.Field()
    # source_page_body = scrapy.Field()
    # crawl_url = scrapy.Field()
    crawl_timestamp = scrapy.Field()

    pass

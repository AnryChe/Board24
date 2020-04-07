# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousesItem(scrapy.Item):
    # Dirty items from site
    _id = scrapy.Field()
    ad_head = scrapy.Field()
    ad_text = scrapy.Field()
    link = scrapy.Field()


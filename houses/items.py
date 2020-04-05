# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    p_head = scrapy.Field()
    price = scrapy.Field()
    h_sqr = scrapy.Field()
    h_rooms = scrapy.Field()
    link = scrapy.Field()
    curency = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from houses.items  import HousesItem
from houses.spiders.rub_houses import RubHousesSpider


class HousesPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.houses_board24


    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        self.text_processing(item)
        collection.insert_one(item)
        return item


    def text_processing(self, item):
        # sity_name = input('Insert sity name: ')
        sity_name = 'РУБЕЖНОЕ'
        if sity_name in item.ad_text:
            return item


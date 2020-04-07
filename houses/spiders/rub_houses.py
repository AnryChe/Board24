# -*- coding: utf-8 -*-
import scrapy
import pprint
from scrapy.http import HtmlResponse
from houses.items  import HousesItem

class RubHousesSpider(scrapy.Spider):
    name = 'rub_houses'
    allowed_domains = ['board24.lg.ua/real/sell/house/']
    start_urls = ['http://board24.lg.ua/real/sell/house//']

    def parse(self, response:HtmlResponse):
        dirty_links = response.xpath('//div[@align]/a[@href]/@href').extract_first()
        yield response.follow(dirty_links, callback=self.parse)
        # print(dirty_links)
        ad_list = response.xpath("//a[@class='doska1']/@href").extract()
        for link in ad_list:
            yield response.follow(link, callback=self.ad_parse)

    def ad_parse(self, response: HtmlResponse):
        ad_head = response.xpath("//div[@class='portlet mess ']/text()").extract()[0]  # Экстракт не полностью помогает, выдает список. Если чезер css - проще и лучше
        ad_text = response.xpath("//td[@class='usertext ']/text()").extract()
        link = response.url()
        yield HousesItem(ad_head=ad_head, ad_text=ad_text, link=link)


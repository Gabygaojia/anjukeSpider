# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['chengdu.anjuke.com']
    start_urls = ['https://chengdu.anjuke.com/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.items import CategoryItem


class CategorySpider(scrapy.Spider):
    name = "category"
    allowed_domains = ["music.so.com"]
    start_urls = ['http://music.so.com/artist/index.html']

    def parse(self, response):
        for category_a in response.xpath("//div[@class='cate']/ul/li/a"):
            category = CategoryItem()
            category['name'] = str(category_a.xpath("text()").extract()[0])
            category['path'] = str(category_a.xpath("@href").extract()[0])
            yield category

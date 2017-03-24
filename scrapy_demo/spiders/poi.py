# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.items import POIItem
from scrapy.selector import Selector


class PoiSpider(scrapy.Spider):
    name = "poi"
    allowed_domains = ["poi86.com"]
    start_urls = ['http://www.poi86.com/poi/district/1289/1.html']

    def parse(self, response):
        i = 0
        for poi_tr in response.css("table.table>tr"):
            poi = POIItem()
            poi['name'] = poi_tr.xpath('td[1]/a/text()').extract()
            poi['path'] = poi_tr.xpath('td[1]/a/@href').extract()
            poi['address'] = poi_tr.xpath('td[2]/text()').extract()
            yield poi
            i=i+1
            if i > 2:
                break


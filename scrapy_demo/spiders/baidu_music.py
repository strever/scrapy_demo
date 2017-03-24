# -*- coding: utf-8 -*-
import scrapy


class BaiduMusicSpider(scrapy.Spider):
    name = "baidu_music"
    allowed_domains = ["music.baidu.com"]
    start_urls = ['http://music.baidu.com/']

    def parse(self, response):
        pass

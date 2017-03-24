# -*- coding: utf-8 -*-
import scrapy
from lib.db import DB
from scrapy_demo.items import ArtistItem


class ArtistSpider(scrapy.Spider):
    name = "artist"
    allowed_domains = ["music.so.com", "s.music.so.com"]
    start_urls = []

    def start_requests(self):
        sql = "SELECT * FROM `categories`"
        categories = DB.connect().fetch_all(sql)
        for category in categories:
            #ArtistSpider.start_urls.append('http://music.so.com' + category['path'])
            req = self.make_requests_from_url('http://music.so.com' + category['path'])
            req.meta['category_id'] = category['id']
            yield req

        #ArtistSpider.start_urls = ["http://music.so.com/artist/chinese-male.html"]


    def parse(self, response):
        self.log('已抓取到 %s, 开始分析数据...' % response.url)
        category_id = response.meta['category_id']
        for section_div in response.xpath('//div[@class="section"]'):
            for li in section_div.xpath("ul/li"):
                artist = ArtistItem()
                artist['category_id'] = category_id
                artist['name'] = str(li.xpath("a/text()").extract()[0])
                artist['path'] = str(li.xpath("a/@href").extract()[0])
                #yield artist
                req = scrapy.Request(artist['path'], callback=self.parse_detail)
                req.meta['artist'] = artist
                yield req

    def parse_detail(self, response):
        artist = response.meta['artist']
        #avatar = response.xpath('//div[@class="pic"]/span/img/@src').extract()[0]
        avatar = response.xpath('//div[@id="js-monitor-star"]//img/@src').extract()
        if avatar:
            avatar = str(avatar[0])
        else:
            avatar = ''
        artist['avatar'] = avatar
        return artist
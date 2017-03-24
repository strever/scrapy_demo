# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ArtistItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    path = scrapy.Field()
    avatar = scrapy.Field()
    category_id = scrapy.Field()


class CategoryItem(scrapy.Item):
    cate_id = scrapy.Field()
    name = scrapy.Field()
    path = scrapy.Field()

class POIItem(scrapy.Item):
    name = scrapy.Field()
    path = scrapy.Field()
    address = scrapy.Field()

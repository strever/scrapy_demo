# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

from lib.db import DB


class CategoryPipeline(object):

    def process_item(self, item, spider):
        item_name = item.__class__.__name__
        if item_name == 'CategoryItem' and item['name'] and item['path']:
            sql = "INSERT INTO `categories`(`name`, `path`) VALUES(%s, %s)"
            DB.connect().execute(sql, (item['name'], item['path']))
            return item
        else:
            raise DropItem('item由于不完整被丢弃')


class ArtistPipeline(object):

    def process_item(self, item, spider):
        item_name = item.__class__.__name__
        print(item)
        if item_name == 'ArtistItem' and item['name'] and item['path']:
            sql = "INSERT INTO `artists`(`name`, `path`, `category_id`, `avatar`) VALUES(%s, %s, %s, %s)"
            DB.connect().execute(sql, (item['name'], item['path'], item['category_id'], item['avatar']))
        return item


class POIPipeline(object):

    def process_item(self, item, spider):
        item_name = item.__class__.__name__
        if item_name == 'POIItem' and item['name'] and item['path']:
            pass
        return item

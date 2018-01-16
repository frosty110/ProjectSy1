# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class TutorialPipeline(object):
    def process_item(self, item, spider):
        print('ITEM PRINT', item)

        validItem = True

        if validItem:
            return item
        else:
            raise DropItem('invalid item %s' % item)

import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = {}
        for k, v in item.items():
            if isinstance(v, bytes):
                item[k] = v.decode("utf-8")

        # json.dumps( {k : v.decode("utf-8") } )  + "\n"
        print('LINE PRINT', item.items())
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item


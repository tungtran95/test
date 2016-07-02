# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from django.db import transaction

from stackover.models import Stackover


class StackoverflowPipeline(object):
    def process_item(self, item, spider):
            scraps = Stackover(**item)
            scraps.save()
            return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class GithubPipeline(object):
    def __init__(self) -> None:
        self.client = MongoClient(host='localhost', port=27017)

        self.col = self.client['githubdata']

        self.githubdata = self.col.githubdata

        self.githubdata.delete_many({})
    
    def process_item(self, item, spider):
        res = dict(item)
        self.githubdata.insert_one(res)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

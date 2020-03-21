# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_name = scrapy.Field()

    author = scrapy.Field()

    star = scrapy.Field()
    
    language = scrapy.Field()

    date = scrapy.Field()
    
    url = scrapy.Field()


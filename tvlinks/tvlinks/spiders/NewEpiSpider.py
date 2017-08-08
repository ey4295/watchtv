import scrapy as scrapy


class NewEpiSpider(scrapy.Spider):
    """check if a new episode has been updated"""
    name='new_epi'
    urls=[
        'http://bbs.ncar.cc/thread-30481-1-1.html',
    ]


    def parse(self, response):
        # get new link
        # check if updated
        # send msg if necessary
        pass

    def add_url(self,url):
        pass

    def set_url(self,url):
        pass

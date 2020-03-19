# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class DoubannvSpider(scrapy.Spider):
    name = 'doubannv'
    allowed_domains = ['doubannv.net']
    start_urls = ['http://www.doubannv.net/html/doubanfuli/index_2.html',
    'http://www.doubannv.net/html/doubanfuli/index_3.html']

    def __init__(self, category=None, *args, **kwargs):
        pass

    def start_requests(self):
        for url in self.start_urls:
            print("请求地址", url)
            yield scrapy.Request(url,self.parse)
        pass

    def parse(self, response):
        # '//img[@class="ui avatar image"]/@src'
        title_list = response.xpath('//img[@class="rounded ui  left image "]/@alt').getall()
        img_list = response.xpath('//img[@class="rounded ui  left image "]/@src').getall()
        img_index_list = response.xpath('//a[@class="imga"]/@href').getall()

        if len(title_list) == len(img_index_list) == len(img_list):
            for i in range(len(title_list)):
                item_title = title_list[i]
                item_img = img_list[i]
                item_index = img_index_list[i]
                item = TutorialItem(title=item_title,img_url=item_img,index_url=item_index)
                print("异步返回数据",item)
                yield item
        
        pass

    # def log(self, response):
    #     pass
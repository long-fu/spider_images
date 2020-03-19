# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# ImagesPipeline 为系统中下载图片的管道
from scrapy.pipelines.images import ImagesPipeline


class TutorialPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print("请求图片数据",item["img_url"])
        # yield scrapy.Request(url=item['img_url'],self.file_path,meta={'item':item})
        yield item["img_url"]

    # def file_path(self, request, response=None, info=None):
    #     item = request.meta['item']
    #     # 设置图片的路径为  类型名称/url地址
    #     # 这是一个图片的url: http://pics.sc.chinaz.com/Files/pic/icons128/7065/z1.png
    #     # 这句代码的意思是先取出图片的url，[0]表示从列表转成字符串
    #     # split分割再取最后一个值，这样写是让图片名字看起来更好看一点
    #     image_name = item['img_url'].split('/')[-1]
    #     print('需要保存的数据',image_name)
    #     # path = '%s/%s' % (item['title'], image_name)
    #     path = item['title'] + image_name
    #     print("保存在当前文件")
    #     return path

# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         print("这里可以下载数据吗")
#         return item

# -*- coding:utf-8 -*-

import os
import urllib
import urllib2
from lxml import etree

class Spider(object):

    def __init__(self):
        self.tiebaName = raw_input("请输入贴吧名称：")
        self.beginPage = int(raw_input("请输入起始页："))
        self.endPage = int(raw_input("请输入终止页："))

        self.url = "http://tieba.baidu.com/f"
        # self.ua_header = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

        self.userName = 1

# class Spider:
#     def __init__(self):
#         self.tiebaName = raw_input("ÇëÐèÒª·ÃÎÊµÄÌù°É£º")
#         self.beginPage = int(raw_input("ÇëÊäÈëÆðÊ¼Ò³£º"))
#         self.endPage = int(raw_input("ÇëÊäÈëÖÕÖ¹Ò³£º"))

#         self.url = 'http://tieba.baidu.com/f'
#         self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

#         self.userName = 1

    def tiebaSpider(self):
      print '进入tiebaSpider'
      for page in range(self.beginPage, self.endPage + 1):
          pn = (page - 1) * 50
          word = {'pn':pn, 'kw':self.tiebaName}
          word = urllib.urlencode(word)
          myUrl = self.url + "?" + word
          print myUrl
          links = self.loadPage(myUrl)


    # def tiebaSpider(self):
    #     for page in range(self.beginPage, self.endPage + 1):
    #         pn = (page - 1) * 50 
    #         word = {'pn' : pn, 'kw': self.tiebaName}

    #         word = urllib.urlencode(word) 
    #         myUrl = self.url + "?" + word

    #         links = self.loadPage(myUrl) 

    def loadPage(self, url):
        print '进入loadPage'
        req = urllib2.Request(url, headers = self.ua_header)

        html = urllib2.urlopen(req).read()

        selector = etree.HTML(html)

        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        for link in links:
            link = "http://tieba.baidu.com" + link
            self.loadImages(link)
        
    # def loadPage(self, url):
    #     print "======="
    #     req = urllib2.Request(url, headers = self.ua_header)
    #     html = urllib2.urlopen(req).read()


    #     selector=etree.HTML(html)

    #     links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    #     print links

    #     for link in links:
    #         link = "http://tieba.baidu.com" + link
    #         self.loadImages(link)
    




    def loadImages(self, link):
        print '进入loadImages'
        req = urllib2.Request(link, headers = self.ua_header)
        html = urllib2.urlopen(req).read()

        selector = etree.HTML(html)
        imagesLinks = selector.xpath('//img[@class="BDE_Image"]/@src')
        for imageLink in imagesLinks:
            self.writeImage(imageLink)

    # def loadImages(self, link):
    #     req = urllib2.Request(link, headers = self.ua_header)
    #     html = urllib2.urlopen(req).read()

    #     selector = etree.HTML(html)

    #     imagesLinks = selector.xpath('//img[@class="BDE_Image"]/@src')

    #     for imagesLink in imagesLinks:
    #         self.writeImages(imagesLink)

    def writeImage(self, imageLink):
        print "正在存储图片%d"%self.userName
        file = open('./images/' + str(self.userName) + '.png', 'wb')
        image = urllib2.urlopen(imageLink).read()
        file.write(image)
        file.close()
        self.userName += 1

    # def writeImages(self, imagesLink):

    #     print "ÕýÔÚ´æ´¢ÎÄ¼þ %d ..." % self.userName

    #     file = open('./images/' + str(self.userName)  + '.png', 'wb')

    #     images = urllib2.urlopen(imagesLink).read()

    #     file.write(images)

    #     file.close()

    #     self.userName += 1

if __name__ == "__main__":
    mySpider = Spider()
    mySpider.tiebaSpider()

# if __name__ == "__main__":
#     mySpider = Spider()
#     mySpider.tiebaSpider()
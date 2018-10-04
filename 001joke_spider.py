# -*- coding:utf-8 -*-

import urllib2
import re

class Spider(object):
    """
    段子爬虫类
    """
    def loadPage(self, page):

        url = "http://www.waduanzi.com/page/" + str(page)

        # User-Agent头
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        headers = {'User-Agent' : user_agent}
        # 构造请求
        req = urllib2.Request(url, headers = headers)
        # 得到响应
        response = urllib2.urlopen(req)
        html = response.read()
        pattern = re.compile('<div class="item-content">(.*?)</div>', re.S)
        item_list = pattern.findall(html)
        return item_list

    def printOnePage(self, item_list, page):
        for item in item_list:
            item = item.replace("<br />", "").replace("<br/>", "")
            self.writeToFile(item)

    def writeToFile(self, text):
        myFile = open('./joke.txt', 'a')
        myFile.write(text)
        myFile.write("----------------------------------------------")
        myFile.close()

    def doWork(self):
        self.page = 1
        self.enable = True

        while self.enable:
            try:
                item_list = self.loadPage(self.page)
            except urllib2.URLError as e:
                print e.reason
                continue

            self.printOnePage(item_list, self.page)
            self.page += 1
            print "按回车键继续……"
            print "输入 quit 退出"
            command = raw_input()
            if (command == "quit"):
                self.enable = False
                break
    

if __name__ == "__main__":
    print "请按下回车开始"
    raw_input()

    # 定义一个Spider对象
    mySpider = Spider()
    mySpider.doWork()

    

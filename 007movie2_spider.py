# -*- coding:utf-8 -*-

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?"

headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

formdata = {
    'type':'22',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'10'	
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)

response = urllib2.urlopen(request)

print response.read()
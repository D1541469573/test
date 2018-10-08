# -*- coding:utf-8 -*-

import urllib
import urllib2
import random

proxy_list = [
	{"https" : "115.46.71.226:8123"},
	{"https" : "122.235.250.197:8118"},
	{"https" : "59.58.39.47:9999"}

]

proxy = random.choice(proxy_list)

httpproxy_handler = urllib2.ProxyHandler(proxy)
nullproxy_handler = urllib2.ProxyHandler()

proxySwitch = True

if proxySwitch:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2.build_opener(nullproxy_handler)

url = "http://www.baidu.com/"

request = urllib2.Request(url)

urllib2.install_opener(opener)

response = opener.open(request)

print response.code
print response.read()
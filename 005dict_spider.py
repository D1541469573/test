# -*- coding:utf-8 -*-

import urllib
import urllib2

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"



headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

formdata = {
	"action" : "FY_BY_CLICKBUTTION",	
	"client" : "fanyideskweb",	
	"doctype" : "json",	
	"from" : "AUTO",	
	"i" : "I love you",	
	"keyfrom" : "fanyi.web",	
	"salt" : "1538806122477",	
	"sign" : "39bf649c40bbb77729c847e73c96b23e",	
	"smartresult" : "dict",	
	"to" : "AUTO",	
	"typoResult" : "false",	
	"version" : "2.1"	
	}

data = urllib.urlencode(formdata)
   
request = urllib2.Request(url, data = data, headers = headers)
html = urllib2.urlopen(request)
print html.code
html = html.read()
print html
# -*- coding:utf-8 -*- 

from bs4 import BeautifulSoup
import urllib2
import urllib
import json

def tencent():

	url = "https://hr.tencent.com/"
	request = urllib2.Request(url + "position.php?&start=0#a")
	response = urllib2.urlopen(request)
	resHtml = response.read()

	output = open('tencent.json', 'w')

	html = BeautifulSoup(resHtml, 'lxml')

	result = html.select('tr[class="even"]')
	result2 = html.select('tr[class="odd"]')
	result += result2

	items = []
	for site in result:
		item = {}

		name = site.select('td a')[0].get_text()
		detailLink = site.select('td a')[0].attrs['href']
		catalog = site.select('td')[1].get_text()
		recruitNumber = site.select('td')[2].get_text()
		workLocation = site.select('td')[3].get_text()
		publishTime = site.select('td')[4].get_text()

		item['name'] = name
		item['datailLink'] = detailLink
		item['catalog'] = catalog
		item['recruitNumber'] = recruitNumber
		item['workLocation'] = workLocation
		item['publishTime'] = publishTime

		items.append(item)



	line = json.dumps(items, ensure_ascii = False)
	output.write(line.encode('utf-8'))
	output.close()

if __name__ == "__main__":
	tencent()
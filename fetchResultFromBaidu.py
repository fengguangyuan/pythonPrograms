#http post test
# _*_ coding: utf-8 _*_
#fetch the searched results from baidu.com
import urllib.request
import urllib.parse
import sys
import re
from bs4 import BeautifulSoup

data = {"wd":"动漫图片"}
url = "https://www.baidu.com/s?"
url2="https://www.baidu.com/s?wd=%E5%8A%A8%E6%BC%AB%E5%9B%BE%E7%89%87"
Agents={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def parseParam(data):
	s = ''
	for key, value in data.items():
		s = '&'+key+'='+value
		print(s)
	if url.rindex('&')+1==len(url):
		return s[1:]
	return s

def getHtml():
	print(data)
	#trans the dictionary to a string
	#s = urllib.parse.urlencode(data)

	#get a request through the agent
	req = urllib.request.Request(url2,headers=Agents)

	#send request and receive the response
	res = urllib.request.urlopen(req)

	content = res.read()
	
	#return all the searched web sites 
	webList = getWebList(content)
	
	newcon = content.decode("gbk",'ignore')
	file = open('test.html','w')
	file.write(newcon)
	file.close()
	#print(content)
	return newcon.encode("utf-8").decode("utf-8")

def getWebList(content):
	soup = BeautifulSoup(content)
	#soup_entries = soup.find(attrs={'class':'t'})
	#soup_entries = soup.find_all(attrs={'class':'t'})
	soup_entries = soup.find_all(class_='t')
	#soup_entries = soup.find("<h3 class=\"t\">.*?<\/h3>")''This statement isnt expected
	
	for h in soup_entries:
		webList = []
		print(h)
		print('\n')
		print(type(h))
		print('\n')
		for c in h.find_all('a'):
			print(c.get('href'))
			webList.append(c.get('href'))
			print(type(c))
			print('\n')
	return webList
	
def getLinkList(text):
	#regex = "<a(.*?)href = \"(.*?)link\?url=(.*?)\">.*<\/a>"
	regex = "<a(.*?)href = \"(.*?)link\?url=(.*?)\">.*<\/a>"
	res = re.compile(regex)
	linkList = re.findall(res,text)
	for link in linkList:
		print(link)
		print('\n')
	print(len(linkList))
#print(parseParam(data))	

getLinkList(getHtml())

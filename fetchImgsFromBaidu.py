#coding = utf-8
#python test 
import re
import os
import urllib.request

gPath = 'photos'

def initPath():
	if(os.path.exists(gPath) == False):
		os.mkdir('gPath')

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	if html == 'null':
		print('No results found!')
	return html.decode("utf-8")


def downloadImg(imgList):
	x = 0
	for img in imgList :
		right = img.rindex('/')
		name = img.replace(img[:right+1],'')
		savepath = gPath + name
		urllib.request.urlretrieve(img,'%s.jpg'%(savepath))
		print(name+ ' save successuflly!\n')
	
def getImg(html):
	initPath()
	reg = r'\"objURL\":\"(.+?\.jpg)\"'
	imgre = re.compile(reg)
	imgList = re.findall(imgre,html)
	downloadImg(imgList)
	
html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B6%AF%C2%FE%CD%BC%C6%AC&fr=ala&ori_query=%E5%8A%A8%E6%BC%AB%E5%9B%BE%E7%89%87&ala=0&alatpl=sp&pos=0")
if __name__ == '__main__' :
	getImg(html)

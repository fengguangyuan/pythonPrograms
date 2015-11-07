#_*_ coding: utf-8 _*_
import shutil
import os
import re
import urllib
import PythonAgent
from bs4 import BeautifulSoup

basepath = ['b:\\','d:\\','e:\\']
directory = 'photos'
aAttrs = ['original','src']
def location():
	for base in basepath:
		if os.path.exists(base) == True:
			if os.path.exists(os.path.join(base,directory)) == False:
				os.mkdir(os.path.join(base,directory))
				print("-------- generate temp directory --------")
				print("---"+os.path.join(base,directory))
				print("-----------------------------------------")
			return os.path.join(base,directory)

#search all the htmls including pictures, then return a list
def openPicWeb(url):
	picUrls = []
	html = PythonAgent.urlOpenWithRead(url)
	soup = BeautifulSoup(html)
	li_entries = soup.find_all('li',class_='img')
#	for li in li_entries:
		#print(li.contents[0].attrs['original'])
#		picUrls.append(li.contents[0].attrs['original'])
	if len(li_entries) < 1:
		li_entries = soup.find_all('img')
		for li in li_entries:
			#print(li.contents[0].attrs['original'])
			picUrls.append(li.attrs['src'])
	return picUrls

#download the exact pics
def retrievePicture(url):
	pictures = openPicWeb(url)
	print()
	path = location()
	n = 0
	for pic in pictures:
		filename = pic[pic.rindex('/'):]
		local = path + str(n++)+'.jpg'
		print(pic)
		#with urlretrieve, get unexpected result.So use another way(save as a file)!
		#urllib.request.urlretrieve(url,local,downloadProcess)
		PythonAgent.retrieveAsFile(url,local)
	
if __name__ == '__main__':
	retrievePicture('http://www.youqu.net/neihantu/dongmantu/')

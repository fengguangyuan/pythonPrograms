#_*_ coding: utf-8 _*_
import urllib.request

Agents={'User-Agent':'<a href="https://www.baidu.com/s?wd=Mozilla&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YvmH6snWfvnWmvnWfsrj0k0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1cknHTzPjcsn1cYrHm3nHm1njT" target="_blank" class="baidu-highlight">Mozilla</a>/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',\
		'Cache-Control':'no-cache'}

def urlOpenWithRead(web):
	req = urllib.request.Request(web,headers = Agents)
	res = urllib.request.urlopen(req)	
	return res.read()

def urlOpen(web):
	req = urllib.request.Request(web, headers = Agents)
	res = urllib.request.urlopen(req)
	return res

def downloadProcess(blocksDone,blockSize,fileSize):
	percentage = 100.0*blocksDone*blockSize/fileSize
	if percentage > 100:
		percentage = 100
	print('%.2f%%' % percentage)	

def retrieveAsFile(url,local):
		res = urlOpen(url)
		with open(local,'wb') as f:
			f.write(res.read())
			
def retrieve(url,local):
	urllib.request.urlretrieve(url,local,downloadProcess)

#_*_ coding: utf-8 _*_
import urllib.request
import re
import SavePicture
import PythonAgent
from bs4 import BeautifulSoup

home_page_flag=['首页','home']

#function for test
def printWeb(html):
	print(html.decode('utf-8'))
#trans the original website to BeautifulSoup one	
def getBSHtml(html):
	return(BeautifulSoup(PythonAgent.urlOpenWithRead(html)))

#fetch all the sub websites and the home page		
def parseSubWeb(html):
	homesite = 'www.youqu.net'
	subsites = []
	ul_entries = html.find_all('ul')
	print(str(len(ul_entries))+' <ul>s')
	for ul in ul_entries:
		print('####### ul ########')
		print(ul.text)
		for li in ul.find_all('li'):
			print("########## li #########")
			#print(li.find('a').get('href'))
			#first step to filter out the unuseful website
			if li.find('a').get('title') or li.find('a').get('class') in home_page_flag:
				homesite = li.find('a').get('href')
			elif not li.find('a').get('href').endswith('.html'):
				continue
			else:
				subsites.append(li.find('a').get('href'))
	preDownload(homesite, subsites)

#join the home page and the sub pages
def joinHomeSub(home, sub):
	if home.endswith('/'):
		tmp = sub[1:]
		home += tmp
	else:
		home += sub
	return home
	
#Use the home site and its sub sites to download what u want
def preDownload(homePage, subWebs):
	print("######### enter into download process ##########")
	print(homePage)
	print(str(len(subWebs))+' sub websites:')
	for web in subWebs:
		print(joinHomeSub(homePage,web))
		print('\n')
		startDownload(joinHomeSub(homePage, web))
	regex_1 = ""

def startDownload(web):
	print('-------- start -------')
	print('\n')
	SavePicture.retrievePicture(web)
	print('--------- end --------')
	print('\n')
	
def retrieveWebList(list):
	print('############# download.py start!! ##############')
	for web in list :
		print('####### start to parse '+web+' #########')
		parseSubWeb(getBSHtml(web))
		

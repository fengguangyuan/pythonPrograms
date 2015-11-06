#_*_ coding: utf-8 _*_
import urllib.request
import re
def openWeb(site):
	req = urllib.request.urlopen(site)
	content = req.read().decode('utf-8')
	print(content)

	
def startDownload(content)
'''
Next steps for downloading pics:
firt page:	<ul>
				<li>
					<a href='#'>
			...

second page:
			<ul>
				<li>
					<a href='#'>
			.....
			
finally:	start to download pics(match all the *.jpg|*.jpeg)
'''
	regex_1 = ""


def retrieveWebList(list):
	for web in list :
		openWeb(web)
		

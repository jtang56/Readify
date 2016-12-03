import urllib2
from bs4 import BeautifulSoup

#Given url, uses urllib2 library to get HTML source
#which_url: URL of webpage to retrieve
def obtainURL(which_url):
	response = urllib2.urlopen(which_url)
	html_doc = response.read()
	return html_doc

#Asks user for a valid URL (copy and paste words best)
#Calls function to process the URL and return HTML source
#Returns HTML source as a string
def queryURL(url):
	#url = raw_input("Enter in your url: ")
	return obtainURL(url)
	#return obtainURL("http://money.cnn.com/2016/10/26/technology/smartwatch-sales-apple/index.html?iid=ob_homepage_tech_pool")
	#return obtainURL("http://www.kenrockwell.com/canon/5d-mk-iv.htm")


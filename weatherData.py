#-*- coding: utf-8 -*-

import urllib
#from urllib import urlretrieve
from BeautifulSoup import *
#import os
import csv 
f=open('Weather_Data2.csv','w')



for year in range(2010,2014):

	for month in range(1,13):
	
		url="https://www.wunderground.com/history/airport/KATT/{0}/{1}/1/MonthlyHistory.html?req_city=Austin&req_state=TX&req_statename=&reqdb.zip=78701&reqdb.magic=1&reqdb.wmo=99999&MR=1&format=1".format(year,month)
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)
		data= soup.prettify()
		f.write(data)
	
	
	


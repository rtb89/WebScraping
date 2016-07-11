
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count=int(raw_input('Enter Count:'))
pos=int(raw_input('Enter Position:'))
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
print "Retrieving:",url

for i in range(count):
	tags = soup('a')
	tag= tags[pos-1]
	url=tag.get('href', None)
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	print "Retrieving:",url

name=re.findall('known_by_(\S+).html',url)
print name
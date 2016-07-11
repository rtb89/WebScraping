

import re
url= "http://python-data.dr-chuck.net/known_by_Fikret.html"

name=re.findall('known_by_(\S+).html',url)
print name
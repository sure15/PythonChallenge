#http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib.request
import re
#keynumber=['12345']
#keynumber=['8022']
keynumber=['63579']
b=0
for a in range(400):
    f=urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+keynumber[0])
    firstLine=str(f.read())
    keynumber=re.findall(r'([0-9]+)',firstLine)
    if len(keynumber)>1:
        break
    b=b+1
    print(keynumber,b)

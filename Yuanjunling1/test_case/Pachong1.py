import urllib2
respuest = urllib2.Request("http://boss.qa.great-tao.com")
response = urllib2.urlopen(respuest)
print response.read()

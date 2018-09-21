#-coding:UTF8-*-
import urllib2,urllib
url = 'https://api.douban.com/v2/book/user/ahbei/collections'
data={'status':'read','rating':3,'tag':'小说'}
data = urllib.urlencode(data)
url2 = urllib2.Request(url,data)
response = urllib2.urlopen(url2)
apicontent = response.read()
print  apicontent

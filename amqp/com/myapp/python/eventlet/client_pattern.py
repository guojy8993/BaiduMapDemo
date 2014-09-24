#author guojingyu
#date      Sep 18, 2014
import eventlet
import urllib2

urls = ["http://www.baidu.com",
     "http://www.sina.com",
     "http://3g.qq.com"]
def fetch(url):
    return urllib2.urlopen(url).read()
pool = eventlet.GreenPool(3)
'''    
if __name__=="__main__":
    print fetch(urls[2])
'''

for body in pool.imap(fetch,urls):
    print "\n\n%s"%len(body)
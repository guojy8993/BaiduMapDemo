#author guojingyu
#date      Sep 25, 2014
from routes import Mapper
m = Mapper()
m.connect("/feeds/{category}/atom.xml",controller="feeds",action="atom")
m.connect("history","/archives/by_eon/{century}",controller="archives",action="aggregate")
m.connect("article","/article/{section}/{slug}/{page}.html",controller="article",action="view")

#inline | requirement 
m.connect(R"/blog/{id:\d+}")
m.connect(R"/{action}/{platform:windows|mac}/{filename}")

url_eg = "/blog/20140809"
print m.match(url_eg)
url_eg2 = "/download/mac/The_Profile_of_Obama"
res = m.match(url_eg2)
print type(res)
print res

 


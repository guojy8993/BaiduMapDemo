#author guojingyu
#date      Sep 25, 2014
from routes import Mapper
m = Mapper()
m.connect("/feeds/{category}/atom.xml",controller="feeds",action="atom")
m.connect("history","/archives/by_eon/{century}",controller="archives",action="aggregate")
m.connect("article","/article/{section}/{slug}/{page}.html",controller="article",action="view")

#inline | requirement 
m.connect(R"/blog/{id:\d+}")
m.connect(R"/{action}/{platform:windows|mac}/{filename}") #Requirements --inline
m.connect("/books/{id}",requirements={"id":R"\d+"})
m.connect("/download/{platform}",requirements={"platform":R"windows|mac"})

url_eg = "/blog/20140809"
print m.match(url_eg)

url_eg2 = "/download/mac/The_Profile_of_Obama"
res = m.match(url_eg2)
print type(res)
print res

url_eg3 = "/download/windows"
print m.match(url_eg3)

url_eg4 = "/books/2333"
print m.match(url_eg4)

 


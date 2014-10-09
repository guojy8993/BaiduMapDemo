#author guojingyu
#date      Sep 26, 2014
from routes import Mapper 
from routes.util import URLGenerator
map = Mapper()
url = URLGenerator(map,dict())
map.connect("archives","/archives/{id}",controller="archives",action="view",id=1)
url("blog",id=123)
url("blog")

print map
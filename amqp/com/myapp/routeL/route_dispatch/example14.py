#author guojingyu
#date      Sep 26, 2014
from routes import Mapper 
map = Mapper()
map.resource("message","messages",collection={"rss":"GET"})
print map
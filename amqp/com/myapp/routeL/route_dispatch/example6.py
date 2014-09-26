#author guojingyu
#date      Sep 26, 2014
#Wildcard routes Demo
from routes import Mapper 
m = Mapper()
#m.connect("/static/{filename:.*?}")
m.connect("/static/{filename:.*?}/download")
#print m.match("/static/longs/1234d21s.jpg")
print m.match("/static/123/download")
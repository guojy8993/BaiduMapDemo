#author guojingyu
#date      Sep 25, 2014
#setup a mapper
from routes import Mapper
mapper = Mapper()
mapper.connect(None,"/error/{action}/{id}",controller="error")
mapper.connect("home","/",controller="main",action="index")

result = mapper.match("/error/myapp/4")
print result

result = mapper.match("/")
print result

















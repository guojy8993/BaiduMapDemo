#author guojingyu
#date      Sep 26, 2014

from routes import Mapper 
map = Mapper()
with map.submapper(controller="home",path_prefix="/admin") as m:
    m.action("home",action="splash")
    m.link("index")
    
#now we parse the route
"""
Route name Methods Path                 
home       GET     /admin{.format}      
index_home GET     /admin/index{.format}
"""
print map
print map.match("/admin.xml")
print map.match("/admin")
print map.match("/admin/index")
print map.match("/admin/index.jsp")





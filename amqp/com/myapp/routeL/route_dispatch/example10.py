#author guojingyu
#date      Sep 26, 2014
from routes import Mapper

map = Mapper()
with map.submapper(controller="home", path_prefix="/admin") as m:
    m.connect("admin_users", "/users", action="users")
    m.connect("admin_databases", "/databases", action="databases")

print map    
print map.match("/admin/users")
print map.match("/admin/databases") #Notice that url must declare prefix in argument [url]
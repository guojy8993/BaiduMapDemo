#author guojingyu
#date      Sep 26, 2014
from routes import Mapper 
from routes.route import Route 
map = Mapper()
map.connect("home","/admin/courses/add",controller="courseController",action="addCourse")
r1 =Route("home2","/admin/subjects/add",controller="subjects",action="subjects")
r2 =Route("home3","/admin/roles/add",controller="roles",action="roles")
map.extend([r1,r2])
print map
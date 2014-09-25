#author guojingyu
#date      Sep 25, 2014
from routes import Mapper
m = Mapper()

m.connect("/blog/{id}")
m.connect("/{library_no}/{section}/{category}")

print m.match("/blog/234556")
print m.match("/010_0001/e3/math")
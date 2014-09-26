#author guojingyu
#date      Sep 26, 2014
from routes import Mapper 
m = Mapper()
EXTENSION_FORMAT = {"ext":R"json|xml"}
m.connect("/entries/{id}{.ext}",requirements=EXTENSION_FORMAT)
print m.match("/entries/123")
print m.match("/entries/123.xml")
print m.match("/entries/123.json")

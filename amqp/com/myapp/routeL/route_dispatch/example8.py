#author guojingyu
#date      Sep 26, 2014
from routes import Mapper 

map = Mapper()
with map.submapper(controller="home") as m:
    m.connect("home","/",actions="splash")
    m.connect("index","/index",actions="index")
    
'''
m = map.submapper(controller="home")
m.connect("home", "/", action="splash")
m.connect("index", "/index", action="index")
'''

print map.match("/")
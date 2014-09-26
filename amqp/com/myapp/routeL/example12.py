#author guojingyu
#date      Sep 26, 2014

from routes import Mapper
map = Mapper()

with map.submapper(controller="entries",path_prefix="/entries",actions=["index","update","new","create","delete"]) as entries:
    entries.submapper(path_prefix="/{id}",actions=["show","new","create","edit"])
print map
print map.match("/entries") # -X GET
print map.match("/entries.xml") # -X GET
print map.match("/entries/3ws2434/edit")
print map.match("/entries/3ws2434.json")
print map.match("/entries/3ws2434/new.xml")
    
'''
Route name     Methods Path                       
index_entries  GET     /entries{.format}     # -X GET     
update_entries PUT     /entries{.format}          
delete_entries DELETE  /entries{.format}  
        
entries        GET     /entries/{id}{.format}     
new_entries    GET     /entries/{id}/new{.format} 
create_entries POST    /entries/{id}{.format}     
edit_entries   GET     /entries/{id}/edit{.format}

{'action': u'index', 'controller': u'entries', 'format': None}
{'action': u'index', 'controller': u'entries', 'format': u'xml'}
{'action': u'edit', 'controller': u'entries', 'id': u'3ws2434', 'format': None}
{'action': u'show', 'controller': u'entries', 'id': u'3ws2434', 'format': u'json'}
{'action': u'new', 'controller': u'entries', 'id': u'3ws2434', 'format': u'xml'}
'''    




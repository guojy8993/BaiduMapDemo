#author guojingyu
#date      Sep 26, 2014
from routes import Mapper 

map = Mapper()
with map.submapper(controller="entries",path_prefix="/entries") as entries:
    entries.index()
    with entries.submapper(path_prefix="/{id}") as entry:
        entry.show()
        #pass
        
print map
print map.match("/entries")
print map.match("/entries.xml")
print map.match("/entries/1s123sd")
print map.match("/entries/1s123sd.xml")


'''
Route name    Methods Path                  
index_entries GET     /entries{.format}     
entries       GET     /entries/{id}{.format}

{'action': u'index', 'controller': u'entries', 'format': None}
{'action': u'index', 'controller': u'entries', 'format': u'xml'}
{'action': u'show', 'controller': u'entries', 'id': u'1s123sd', 'format': None}
{'action': u'show', 'controller': u'entries', 'id': u'1s123sd', 'format': u'xml'}
'''


routes.Mapper使用的一些注意事项:(以 m = Mapper() 举例)
1.m 必须 先把 映射关系 connect完毕 再使用;边connect边使用会匹配出None
e.g:
   (1)这样是错误的:
	   m.connect("/blog/{id}")
	   print m.match("/blog/234556") # {'id': u'234556'}
	    
	   m.connect("/{library_no}/{section}/{category}")
	   print m.match("/010_0001/e3/math") #None
    
   (2)这样是正确的:
	   m.connect("/blog/{id}")  
	   m.connect("/{library_no}/{section}/{category}") 
	   
	   print m.match("/blog/234556") #{'id': u'234556'}
	   print m.match("/010_0001/e3/math") #{'category': u'math', 'section': u'e3', 'library_no': u'010_0001'}
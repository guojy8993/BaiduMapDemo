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
	   
	   

2.避免冲突关键字 controller 
  如:m.connect("/{controller}/{id}")就会导致Mapper失去映射效果,可以换个比如 ctrl 替代 controller 就OK了
   
3.Mapper的connect方法的 requirements 参数是字典类型; 推荐格式是 定义系列数据格式 比如DATE_FORMAT = {"year":R"\d\d\d\d","month":"\d\d","day":"\d\d"}  
  这样可以全局通用，特别是大量的connect,且大量参数验证的时候，减小requirements的体量;
  
4.
#author guojingyu
#date      Sep 25, 2014
import uuid
from abc import abstractmethod
class BaseController(object):
    controller_tag = None
    
    @abstractmethod
    def get(self,sid):
        pass
    
    @abstractmethod
    def update(self,sid,**kwargs):
        pass
    
    @abstractmethod
    def delete(self,sid):
        pass
    
    @abstractmethod
    def list(self):
        pass
    
    @abstractmethod
    def add(self,**kwargs):
        pass
    
    
class BookController(BaseController):
    controller_tag = "Book"
    def get(self,sid):
        print "Here is info of Book-%s: ..."%str(sid)
    def update(self,sid,**kwargs):
        author = kwargs.get("author","")
        publish_at = kwargs.get("publish_at","")
        print "Update info of Book-%s : Author %s - Written in %s - Description -"%(str(sid),author,str(publish_at))
    def delete(self,sid):
        print "Book-%s deleted !"%str(sid)
    def list(self):
        print "The stored books are all here as follows: ..."
    def add(self,**kwargs):
        author = kwargs.pop("author")
        publish_at = kwargs.pop("publish_at")
        sid = uuid.uuid4()
        print "Add new Book-%s : Author %s - Written in %s - Description -"%(str(sid),author,str(publish_at))
        
class ProductController(BaseController):
    controller_tag = "Product"
    def get(self,sid,**kwargs):
        print "Here is info of Product-%s:..."%str(sid)
    def update(self,sid,**kwargs):
        city = kwargs.get("city","")
        produce_at = kwargs.get("produce_at","")
        print "Update info of Product-%s : Produced in  %s - Produced at %s - Description -"%(str(sid),city,str(produce_at))
    def delete(self,sid):
        print "Product-%s sale out !"%str(sid)
    def list(self):
        print "The stored Products are all here as follows: ..."
    def add(self,**kwargs):
        city = kwargs.pop("city")
        produce_at = kwargs.pop("produce_at")
        sid = uuid.uuid4()
        print "Add new product-%s Produced in  %s - Produced at %s - Description -"%(str(sid),city,produce_at)
        
"""        
if __name__=="__main__":
    book_info = dict()
    book_info["author"] = "Julia"
    book_info["publish_at"] = 2003
    
    bookController = BookController()
    bookController.list()
    
    bookController.get("1g3b3b445bn3")
    
    bookController.update("1g3b3b445bn3",**book_info)
    
    bookController.delete("1g3b3b445bn3")
    print bookController.controller_tag
    
       
    
    product_info = dict()
    product_info["produce_at"] = 2012
    product_info["city"]= "SuZhou"
    
    productController = ProductController()
    productController.list()
    productController.get("1323xcvw4sd")
    productController.update("1323xcvw4sd",**product_info)
    productController.delete("1323xcvw4sd")
    print productController.controller_tag
"""
    
bookController = BookController()
productController = ProductController()
    
    
    
    
    
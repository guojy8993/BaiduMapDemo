#author guojingyu
#date      Sep 25, 2014
import controllers
from routes import Mapper

RESOURCES = ["book","product"]
class Manager(object):
    def __init__(self):
        self.mapper = Mapper()
        self.mapper.connect("/{param1}/{param2}")
        self.mapper.connect("/{param1}/{param2}/{sid}")
        self.controllers = {}
        for resource in RESOURCES:
            self.controllers[resource]= getattr(controllers, resource+"Controller")
        
    def process_req(self,req):
        
        url = req["url"]
        kwargs = self.mapper.match(url)
        if "body" in req:           
            kwargs.update(req.get("body"))
        controller = self.controllers.get(kwargs.pop("param1"))
        action = kwargs.pop("param2")
        getattr(controller, action)(**kwargs)
        
if __name__ == "__main__":
      
    """
    m = Mapper()
    m.connect("/{param1}/{param2}")
    m.connect("/{param1}/{param2}/{sid}")
    
    path = "/book/list"
    
    print m.match(path)
    """
    
    manager = Manager()
    #req = {"url":"/book/delete/124344556"}
    #req = {"url":"/book/update/124344556","body":{"publish_at":2001,"author":"Hao"}}
    #req = {"url":"/book/add","body":{"publish_at":2001,"author":"Hao"}}
    req = {"url":"/product/add","body":{"produce_at":2001,"city":"Changshang Hunan"}}
    manager.process_req(req)

    
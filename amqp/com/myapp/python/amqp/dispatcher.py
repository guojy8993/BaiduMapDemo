#author guojingyu
#date      Sep 3, 2014

class RpcDispatcher(object):
    def __init__(self,callback):
        print 'initializing RpcDispatcher with \'callback\' : %s'%str(callback)
        print 'RpcDispatcher \'s callback is Manager\'s instance'
        print 'RpcDispatcher acts as Proxy of ProxyCallback...'
        
        self.callback = callback
        #callback should be instance of class  Manager defined in manager.py
    def dispatch(self,method,**kwargs):
        print 'RpcDispatcher dispatches request : method - %s and params - %s'%(method,str(kwargs))
        print 'RpcDispatcher\'s callback :%s '%str(self.callback)
        if hasattr(self.callback,method):
            print 'hasattr ...'
            return getattr(self.callback,method)(**kwargs)
        msg = 'no such rpc method exception '
        raise Exception(msg) 
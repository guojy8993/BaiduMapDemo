#author guojingyu
#date      Sep 2, 2014

import impl_kombu

def msg_reply(msg_id,reply):
    msg = {'result':reply}
    conn = impl_kombu.Connection()
    conn.direct_send(msg_id,msg)
    
class ProxyCallback(object):
    
    def __init__(self,proxy):
        self.proxy = proxy
        print 'The proxy of ProxyCallback is instance of RpcDispatcher :%s '%str(proxy)
        
    def __call__(self,message_data):
        method = message_data.get('method')
        args = message_data.get('args',{})
        msg_id = message_data.get('msg_id')
        print 'Receive rpc request and method is %s '%method
        self._process_data(msg_id,method,args)
    
    def _process_data(self,msg_id,method,args):
        print 'ProxyCallback \'s _process_data method ...and args :%s'%str(args)
        print 'ProxyCallback \'s callback :%s'%str(self.proxy)
        rval = self.proxy.dispatch(method,**args)
        print 'After processing data...'
        msg_reply(msg_id,rval)

'''
    The __call__ method acts as the default method to call of ProxyCallback ;
    This ProxyCallback do the following jobs:
    1.parse the message body to get metod to call and args to call with ;
    2.call the Manager to compute the result ;
    3.direct send result to amqp with msg_id (caller exchange);
'''
    
    
        
    
    
    
    
    
    
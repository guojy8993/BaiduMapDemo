#author guojingyu
#date      Sep 3, 2014
import rpc
import manager
import dispatcher

TOPIC = 'sendout_request'

class Service(object):
    def __init__(self):
        self.topic = TOPIC
        self.manager = manager.Manager()
        print 'succeed initializing Service'
    
    def start(self):
        print 'inner service...start..'
        self.conn = rpc.create_connection()
        rpc_dispatcher = dispatcher.RpcDispatcher(self.manager)
        self.conn.create_consumer(self.topic, rpc_dispatcher)
        self.conn.consume()
        print 'succesd starting service..'
        
    def drain_events(self):
        print 'server waiting ...'
        self.conn.drain_events()
        
'''
   Client  ---> amqp ----> Server  then  Client  <--- amqp <---- Server
   Here we find that both client and server need to connect to amqp,in other words,
   they themselves needs a aqqp connection ;  
'''
'''
    server-->service-->RpcDispatcher-->Manager
'''
        
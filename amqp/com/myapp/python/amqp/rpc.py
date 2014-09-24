#author guojingyu
#date      Sep 3, 2014
import impl_kombu

def create_connection():
    return impl_kombu.Connection()
def call(topic,msg,timeout=None):
    print 'the client has passed params to rpc : topic - %s and msg - %s '%(topic,str(msg))
    return impl_kombu.call(topic, msg, timeout)
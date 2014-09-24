#author guojingyu
#date      Sep 3, 2014
import rpc
TOPIC = 'sendout_request'

msg = {'method':'add','args':{'v1':1,'v2':2}}
rval = rpc.call(TOPIC, msg)
print 'succeed implementing RPC call .and the return value is %d '%rval
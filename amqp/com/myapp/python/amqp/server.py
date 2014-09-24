#author guojingyu
#date      Sep 3, 2014

import service

svr = service.Service()
print 'start a server to service......'
svr.start()

while True:
    print 'start to wait for msg to consume ....'
    svr.drain_events()
    #the conn draint_events ...(drain ,here means consume ..)

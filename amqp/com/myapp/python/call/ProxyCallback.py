#author guojingyu
#date      Sep 15, 2014

class DemoProxyCallback(object):
    def __call__(self,name):
        print 'Hello,'+str(name.pop())+' ; This demo shows how to use __call__ ;'
        print len(name)
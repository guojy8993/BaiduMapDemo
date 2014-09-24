#author guojingyu
#date      Sep 15, 2014
import ProxyCallback
name = []
class Caller(object):
    def __init__(self,proxy):
        self.proxy = proxy
    def call(self):
        name.append('Tom')
        self.proxy(name)

if __name__ == '__main__':
    caller = Caller(ProxyCallback.DemoProxyCallback())
    caller.call()
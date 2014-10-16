#author guojingyu
#date      Oct 10, 2014

class Obj(object):
    def test(self):
        print self.__class__.__name__
if __name__ == "__main__":
    o = Obj()
    o.test()
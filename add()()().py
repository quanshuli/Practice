class add(int):__call__ = lambda self, v: add(self+v)

#
class add(int):
    def __call__(self,n):
        return add(self+n)
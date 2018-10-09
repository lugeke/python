class Singleton():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = super().__new__(cls)
        return Singleton.__instance

s = Singleton()
s1 = Singleton()

assert(s is s1)

class SingleDecorator():
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance

class A(): pass

A = SingleDecorator(A)

a = A()
a1 = A()

assert(a is a1)
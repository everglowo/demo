class Hello(object):
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hello,%s"%self.name)

h = Hello("zeze")
h.sayHello()



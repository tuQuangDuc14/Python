class SimpleClass:
    #class attribute
    i=5
    #init
    def __init__(self):
        self.j=7
    #methos
    def printMe(self):
        print(self.j)
    
objectA= SimpleClass()
objectB= SimpleClass()

objectA.printMe()
print(objectB.i)

#thu truy cap k phai static
class SimpleClass2:
    #contructor
    def __init__(self):
        self.name="duc"
    #methos
    def hello(self):
        print("hello "+ self.name)
    #static methos
    @staticmethod
    def hi(name):
        print("hi " + name)

objectc= SimpleClass2()
objectd= SimpleClass2()

objectc.hello()
objectd.hi("duc1")
SimpleClass2.hi("duc1")
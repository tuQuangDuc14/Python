#bai tap ve dong vat
#xay dung class cha

class Animal:
    #contructor: xay dung ra doi tuong
    def __init__(self, animalTypeA, nameA, widthA, heightA, weightA):
        self.animalType = animalTypeA
        self.name = nameA
        self.width = widthA
        self.height = heightA
        self.weight =weightA

    #method
    #phat ra tieng keu
    def makeVoice(self):
        print("unknow")
    def printme(self):
        print("animalType:{0}, name : {1}, width = {2}, height = {3}, weight = {4}".format(self.animaltype, self.name,self.width,self.height,self.weight))
    
a1=Animal("nguoi","gfgfgf","22","fhhfhf","hhdh")   
a1.makeVoice()
a1.printme()

#class ke thua 
class Dog(Animal):
    #contructor
    def __init__(self, nameA, widthA, heightA, weightA, ColorA):
        #goi contructor cua cha
        Animal.__init__(self, "Dog",nameA, widthA, heightA, weightA)
        #gan 
        self.Color =ColorA

    def makeVoice(self):
        print("{0} : meo meo".format(self.name))
        print(self.color)

cat1 = Dog("mui",)
cat1.makeVoice()
cat1.printme()
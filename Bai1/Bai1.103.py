# Python Classes/Objects
class MyClass:
  x = 5
  name = "duc"

p1 = MyClass()
print(p1.x)
print(p1.name)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  

p1 = Person("John", 36)

print(p1.name, p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self, high):
    print("Hello my name is " + self.name)
    print("Hello my high is ", high)

p1 = Person("John", 36)
p1.myfunc(12)
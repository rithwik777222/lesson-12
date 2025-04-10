class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
      print('i am a cat,','my name is',self.name,"i am",self.age,'years old.')

    def sound(self):
       print('meow')

class dog:
    def __init__(self,name,age):
       self.name = name
       self.age = age

    def info(self):
       print("i am a dog,","my name is",self.name,"i am",self.age,"years old.")

    def sound(self):
       print("bark")

cat1 = cat('isaac meowton',7)
dog1 = dog('sir barks',12)

for animal in (cat1,dog1):
   animal.sound()
   animal.info()
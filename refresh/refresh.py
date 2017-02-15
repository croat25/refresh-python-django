name = "Julie"

age = 42

sentence = print("Hi my name is {} and I am {} years old".format(name,age))

if age > 18:
	sentence
elif age > 25:
	sentence
else:
	sentence


def Hello(name,age):
	print("Hello {}, you are {} old".format(name,age))


Hello("Bruno",25)


dog=["Fido","Sean","Sally","Mark"]
print(dog)
dog.insert(0,"Bruno")
print (dog)
print (dog[2])
print(len(dog))

for i in dog:
	print(i)

for t in range (0,3):
	print (t)

ranged=10
a=0
while a < ranged:
	print(a)
	a+=1

class Dog:
	def __init__(self,name="",age=0,fur="",colour=""):
		self.name=name
		self.age=age
		self.fur=fur
		self.colour=colour
	dogInfo="hey dogs are cool"
	def bark(self,str):
		print("BARK!"+str)



mydog=Dog("bruno",25,"puf","brown")
mydog.bark("hello world")
mydog.name="Bruno"
mydog.age="25"
print(mydog)
print(mydog.age)

print(Dog.dogInfo)
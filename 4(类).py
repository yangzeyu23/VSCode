#类与对象

#定义类
class Car(object):
	pass

car=Car()  
#创建对象


#实例变量
class Dog(object):
	"""docstring for Dog"""
	def __init__(self,name,age,sex="雌性"):  #构造方法
		self.name = name          #创建和初始化实例变量
		self.age = age 
		self.sex = sex

d1=Dog("球球",2)
d2=Dog("哈哈",1,"雄性")
d3=Dog(name="拖布",sex="雌性",age=3)#关键字调用，顺序可以任意指定

print("A家狗狗名叫{0}，{1}岁，性别为{2}。".format(d1.name,d1.age,d1.sex))
print("B家狗狗名叫{0}，{1}岁，性别为{2}。".format(d2.name,d2.age,d2.sex))
print("C家狗狗名叫{0}，{1}岁，性别为{2}。".format(d3.name,d3.age,d3.sex))


#example
class Physics(object):
	def __init__(self,name,nationality,field,influence):
		self.name = name
		self.nationality = nationality
		self.field = field
		self.influence = influence

p1=Physics("Newton","Britain","mechanics","No.1")
p2=Physics("Maxwell","Britain","electrodynamics","No.3")
p3=Physics("Einstein","Germany","relativity","No.2")
p4=Physics("Bohr","Denmark","quantum mechanics","No.4")
p5=Physics("Schrodinger","Austria","quantum mechanics","No.5")

print('''
''')
print("name:{0}\tnationnality:{1}\tfield:{2}\tinfluence:{3}".format(p1.name,p1.nationality,p1.field,p1.influence))
print("name:{0}\tnationnality:{1}\tfield:{2}\tinfluence:{3}".format(p2.name,p2.nationality,p2.field,p2.influence))
print("name:{0}\tnationnality:{1}\tfield:{2}\tinfluence:{3}".format(p3.name,p3.nationality,p3.field,p3.influence))
print("name:{0}\tnationnality:{1}\tfield:{2}\tinfluence:{3}".format(p4.name,p4.nationality,p4.field,p4.influence))
print("name:{0}\tnationnality:{1}\tfield:{2}\tinfluence:{3}".format(p5.name,p5.nationality,p5.field,p5.influence))
print('''
''')

#实例方法
#class Dog:
#	def __init__(self,name,age,sex="雌性"): 
#		self.name = name         
#		self.age = age 
#		self.sex = sex
#
#def run(self):
#	print("{}在跑......".format(self.name))
#
#def speak(self,sound):
#	print("{}在叫，{}！".format(self.name,sound))


#dog=Dog("球球",2)
#dog.run()
#dog.speak("汪汪汪")
#这段代码存在严重问题，但具体不清楚是什么


#类变量
class Account:
	interest_rate = 0.0568            #定义类变量

	def __init__(self,owner,amount):  #定义实例变量
		self.owner = owner
		self.amount = amount

account=Account("Newton",88000.00)

print("账户名:{0}".format(account.owner))
print("账户金额:{0}".format(account.amount))
print("利率:{0}".format(Account.interest_rate))

print('''

账户用名:{0}
账户余额:{1}
账户利息:{2}
'''.format(account.owner,account.amount,Account.interest_rate))



#类方法
class Account:
	interest_rate = 0.045

	def __init__(self,owner,amount):
		self.owner = owner
		self.amount = amount

	@classmethod #定义装饰器，@开头修饰函数
	def interest_by(cls,amt):   #cls:自身即Account类
		return cls.interest_rate*amt

interest = Account.interest_by(10000.00)
print("计算利息:{0:.4f}".format(interest))
#注意类方法可以访问类变量，但不能访问实例变量和实例方法


#example
class Reproduction(object):
	improvement_rate=0.02
	
	def __init__(self,amount):
		self.amount = amount
		
	@classmethod
	def a_(cls,amt):
		return ((1+cls.improvement_rate)**10)*amt

a=Reproduction.a_(100)

print('''
繁殖问题预测:

初始年,兔子的基数为:\t {0:.0f}
兔子年增长率:\t {1:.3f}
则年十后,兔子的繁殖结果为:\t {2:.0f}
'''.format(100,0.02,a))
#疑问:classmethod一次是不是只能调用(访问)一个类变量？
#试了很多次都无济于事，没法将多个量同时访问。



#封装性


#私有变量
class Account:
	__interest_rate = 0.400  #私有类变量

	def __init__(self,owner,amount):
		self.owner=owner
		self.__amount=amount #私有实例变量

	def desc(self):          #在类的内部可以访问私有变量
		print("用户：{0} \n金额：{1} \n利率：{2}".format(self.owner,self.__amount,Account.__interest_rate))

account=Account("Newton",10000.00)
account.desc()

print('''
账户名：{0}'''.format(account.owner))

#以下代码将会有错误发生：
#  print("账户金额：{0}".format(account.__amount))
#  因为在类的外部不可以访问私有变量


#example:
class Reproduction:
	__improvement_rate = 0.02

	def __init__(self,parents,total_amount):
		self.parents=parents
		self.__total_amount=total_amount

	def dww(self):
		print('''
初始值：{0}
最终总数：{1}
变化率：{2}
'''.format(self.parents,self.__total_amount,Reproduction.__improvement_rate))

reproduction=Reproduction(100,122)
reproduction.dww()

print('''
初代总数：{0}'''.format(reproduction.parents))



#私有方法
print('''

''')
class Account:
	__interest_rate = 0.03

	def __init__(self,owner,amount):
		self.owner = owner
		self.__amount = amount

	def __info(self):  #定义私有方法
		return "用户：{0}\n金额：{1}\n利率：{2}".format(self.owner,self.__amount,Account.__interest_rate)

	def desc(self):
		print(self.__info())  #在类的内部调用私有方法

account=Account("Einstein",10000.0)
account.desc()
#发生错误：
#account.__get_info()
#不能在类的外部调用私有方法



#使用属性(使用公有方法访问)
print('''

''')
class Dog:
	
	#构造方法
	def __init__(self,name,age,sex="female"):
		self.name=name
		self.__age=age

	#实例方法
	def run(self):
		print("{0} is running......".format(self.name))
	
	#get方法
	def get_age(self):
		return self.__age #返回私有化实例变量

	#set方法
	def set_age(self,age):
		self.__age = age  #通过age参数更新私有化实例变量

dog=Dog("apple",2)
print("the dog's age:{}".format(dog.get_age()))

dog.set_age(3)
print("after the correction,the dog's age is:{}".format(dog.get_age()))
#通过set()方法赋值
#通过get()方法取值


#若使用属性,调用方法更为简单.示例代码如下:
print('''

''')
class Dog:

	def __init__(self,name,age,sex="female"):
		self.name = name
		self.__age = age 

	def run(self):
		print("{} is running".format(self.name))

	@property
	def age(self):         #替代get_age(self)的get方法
		return self.__age
	
	@age.setter
	def age(self,age):     #替代set_age(self,age)的set方法
		self.__age = age

dog = Dog("haha",2)
print("the dog's age is: {}".format(dog.age))
dog.age = 3                #属性在左边为赋值，右边为取值
print("after the correction,the dog's age is:{}".format(dog.age))
#此时即可通过属性取值，访问方式为“实例.属性”



#继承性

#Python的继承
print('''

''')
class Animal:       #定义父类

	def __init__(self,name):
		self.name = name

	def show_into(self):
		return "the animal's name is:{}".format(self.name)

	def move(self):
		print("keep moving......")

class Cat(Animal):  #定义子类
	
	def __init__(self,name,age):
		super().__init__(name)  
		#调用父类构造方法，初始化父类成员变量
		self.age = age
		#初始化子类实例成员变量

cat = Cat("Austria",8)
cat.move()
print(cat.show_into())
#父类中只有公用的成员变量会被继承！！！


#example
print('''

''')
class Animal:

	def __init__(self,name,age,hobby):
		self.name = name
		self.age = age
		self.hobby = hobby

	def Name_Age_Hobby(self):
		return "这头小猪的名字叫做: {0} \n他的年龄是: {1} \n他的爱好是：{2}".format(self.name,self.age,self.hobby)

class Pig(Animal):

	def __init__(self,name,age,hobby):
		super().__init__(name,age,hobby)
		self.name = name
		self.age = age
		self.hobby = hobby

pig = Pig("张涵宇",9,"下国际象棋")
print("悄悄告诉你：\n"+pig.Name_Age_Hobby())
print('''

''')



#多继承

#定义父类1:
class Horse:
	def __init__(self,name):
		self.name = name

	def show_info(self):
		return "the horse's name:{0}".format(self.name)

	def run(self):
		print("the horse is running......")
#定义父类2:
class Donkey:
	def __init__(self,name):
		self.name = name     #实例变量name

	def show_info(self):
		return "the donkey's name is:{0}".format(self.name)

	def run(self):
		print("the donkey is running......")

	def roll(self):
		print("the donkey is rolling...... ")
#定义子类:
class Mule(Horse,Donkey):  
	def __init__(self,name,age):
		super().__init__(name)
		self.age = age       #实例变量age

m = Mule("Benchi",3)
m.run()                      #继承父类Horse方法(running)
m.roll()                     #继承父类Donkey方法(rolling)
print(m.show_info())         #继承父类Horse方法

#多继承从左至右继承级别从高到低

print('''


''')

#方法重写(override)

class Horse:
	def __init__(self,name):
		self.name = name

	def show_info(self):
		return "the horse's name is: {0}".format(self.name)

	def run(self):
		print("the horse is runnning...")

class Donkey(object):
	def __init__(self,name):
		self.name = name

	def show_info(self):
		return "the donkey's name is: {0}".format(self.name)

	def run(self):
		print("the donkey is running...")

	def roll(self):
		print("the donkey is rolling...")

class Mule(Horse,Donkey):

	def __init__(self,name,age,characteristics):
		super().__init__(name)  
		#注意由于父类Horse只给出了name的参数，此处super的调用不能涉及其他子类自己的参数的
		self.name = name   
		self.age = age
		self.characteristics = characteristics  #初始化子类实例成员变量

	def show_info(self):  #重写父类方法
		return "\nthe mule: \nname:\t{0} \nage:\t{1} years old \ncharacteristics:\t{2}".format(self.name,self.age,self.characteristics)


m = Mule("Benchi",3,"eating")
m.run()                 #继承Horse方法
m.roll()                #继承Donkey方法
print(m.show_info())    #这是子类自己的方法

#在这样的情况下，子类才有真正意义上的表达自由


print('''


''')
#多态性

#继承与多态
class Animal:
	def speak(self):
		print("the animals are barking, but we could not match their sounds with their types!")

class Dog(Animal):
	def speak(self):
		print("the dog is barking as 'wong,wong......'" )

class Cat(Animal):
	def speak(self):
		print("the cat is barking as 'miao,miao......'")

an1 = Dog()
an2 = Cat()
an1.speak()
an2.speak()



print('''


''')



#鸭子类型测试与多态
def start(obj):
	obj.speak()   #设计一个start()函数，使得接收到的对象都具有speak方法

#下面定义几个类，他们都具有speak()方法
class Animal:
	def speak(self):
		print("the animals are barking, but we could not match their sounds with their types!")

class Dog(Animal):
	def speak(self):
		print("the dog shouts as 'wong,wong......'" )

class Cat(Animal):
	def speak(self):
		print("the cat shouts as 'miao,miao......'")
 
class Car:
	def speak(self):
		print("the car shouts as 'di,di,......'")
#由于支持鸭子类型测试，Python不检查发生多态的对象是否继承了同一个父类，只要他们有相同的行为(方法)，他们之间就是多态的
#此处虽然car没有继承animal的父类，但由于已经规定了start函数及其对应的speak方法，所以就会与其他对象形成多态

start(Dog())
start(Cat())
start(Car())





























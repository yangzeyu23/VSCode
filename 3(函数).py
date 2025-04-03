#函数

#定义函数
def trangle_area(width,height):
	area=0.5*width*height
	return area

def print_area(width,height):
	area=0.5*width*height
	return area #可以省略
	print("三角形的面积计算方法为:0.5x{0}x{1},故面积为:{2}".format(width,height,area))


#使用位置参数调用函数
t_area=trangle_area(12,20)
print("三角形的面积计算方法为:0.5x{0}x{1},故面积为:{2:.3f}".format(12,20,t_area))

#调用函数基本格式:实参列表顺序与形参一致


#使用关键字调用函数
t_area=trangle_area(width=12,height=20)
print("三角形的面积计算方法为:0.5x{0}x{1},故面积为:{2:.3f}".format(12,20,t_area))

t_area=trangle_area(height=20,width=12)
print("三角形的面积计算方法为:0.5x{0}x{1},故面积为:{2:.3f}".format(12,20,t_area))

#实参列表顺序不再受限


#example:
def cuboid_volume(length,width,height):
	volume=length*width*height
	return volume

c_volume=cuboid_volume(length=2,width=3,height=4)
print('''

长方体的体积计算公式为:
            	
            	体积=长x宽x高

本题数据:
长：{0:.3f}m
宽：{1:.3f}m
高：{2:.3f}m
故长方体的体积为:{0:.3f}m x{1:.3f}m x{2:.3f}m ={3:.3f}m^3
'''.format(2,3,4,c_volume))


def trapezoid_area(upperbase,bottombase,height):
	area=0.5*(upperbase+bottombase)*height
	return area

t_area=trapezoid_area(upperbase=2,bottombase=4,height=5)
print('''
梯形面积公式为:
				
		面积=0.5x(上底+下底)x高

本题数据:
上底：{0:.3f}cm
下底：{1:.3f}cm
高：{2:.3f}cm
故梯形的面积为:0.5 x ({0:.3f}cm + {1:.3f}cm) x {2:.3f}cm ={3:.3f}cm^3
'''.format(2,4,5,t_area))


#参数的默认值
def make_coffee(name="卡布奇洛"):   #默认值
	return "制作一杯{0}咖啡。".format(name)

coffee1=make_coffee("拿铁")        #提供参数
coffee2=make_coffee()              #未提供参数，为默认值

print(coffee1)
print(coffee2)


#基于元组的可变参数
def sum(*numbers):
	total=0.0
	for number in numbers:
		total+=number
	return total

print(sum(100,20,300,50))  #多个参数被组装成元组numbers
print(sum(1,1,4,5,1,4))


#基于字典的可变参数
def show_info(**info):
	print("——————————show_info——————————")
	for key, value in info.items():
		print("{0}———{1}".format(key, value))

show_info(name="Maxwell",age=100,sex=True)
show_info(student_name="Maxwell",student_number="1000")


def inter_action(**action):
	print('''
————————introduction————————''')
	for key, value in action.items():
		print("{0}————{1}——{1}".format(key, value))

inter_action(name="Newton",age=380,sex="male",reputation="remarkble")
inter_action(number="No.1")

#此处注意第108行，为什么加上这一行就导致多出一个introduction的下划线？


#函数变量作用域

#全局变量
x=20

def test_value():
	x=10
	print("函数中x={0}.".format(x)) #屏蔽全局变量

test_value()
print("全局变量x={}.".format(x))

#取消屏蔽
def test_value():
	global x
	x=10
	print("函数中x={0}.".format(x)) #屏蔽全局变量

test_value()
print("全局变量x={}.".format(x))

#函数类型
def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def calc(opr):
	if opr=="+":
		return add
	else:
		return sub

f1=calc("+")   #调用，实际上f1就是add函数
f2=calc("-")
print('''

10+5的计算结果为:{0:0.2f}.
45-22的计算结果为:{1:d}.
'''.format(f1(10,5),f2(45,22)))

#example:
def square(a):
	return a*a

def judge(w):
	if w=="find":
		return square
	else:
		return 0
f1=judge("find")

s=input("请输入一个正整数:")
print('''
{0:d}的平方为:{1:.2f}

'''.format(int(s),f1(int(s))))


#过滤函数
def f(x):
	return x > 50  #提供过滤函数

data1=[11,35,22,73,63,74,28,27,68,45]

filtered=filter(f,data1)
data2=list(filtered)     #filter返回值不是列表格式
print("在以上列表中，大于50的数有:"+ str(data2))

#映射函数
def h(x):
	return x**0.5  

data1=[11,35,22,73,63,74,28,27,68,45]

mapped=map(h,data1)
data2=list(mapped)    
print('''
映射后的结果列表为:
'''+str(data2))

#匿名函数(节省代码量)
def calc(opr):
	if opr=="+":
		return lambda a,b:(a+b) #参数/lambda体
	else:
		return lambda a,b:(a-b)
f1=calc("+")  
f2=calc("-")
print('''

10+5的计算结果为:{0:0.2f}.
45-22的计算结果为:{1:d}.
'''.format(f1(10,5),f2(45,22)))

#example
data1=[11,35,22,73,63,74,28,27,68,45]

filtered=filter(lambda x:(x>50),data1)
data2=list(filtered)     
print("在以上列表中，大于50的数有:"+ str(data2))


data1=[11,35,22,73,63,74,28,27,68,45]

mapped=map(lambda x:(x**0.5),data1)
data2=list(mapped)    
print('''
映射后的结果列表为:
'''+str(data2))













#异常处理

#除零异常
i =input("please input a number:")

n=666
result = n/int(i)
print(result)
print("{0} divided by {1} is {2}.".format(n,i,result))
#如输入0将导致异常


#捕获异常

#try—except语句

i =input("please input a number:")
n=666
try:
	result=n/int(i)
	print(result)
	print("{0} divided by {1} is {2}.".format(n,i,result))
except:
	print("a number couldn't be divided by 0,发生异常")

#若指定异常类型:
i =input("please input a number:")
n=666
try:
	result=n/int(i)
	print(result)
	print("{0} divided by {1} is {2}.".format(n,i,result))
except ZeroDivisionError as e:
	print("警告,发生异常:{} \n但程序运行将继续---".format(e))


#多个except代码块
i =input("please input a number:")
n=666
try:
	result=n/int(i)
	print(result)
	print("{0} divided by {1} is {2}.".format(n,i,result))
except ZeroDivisionError as e:
	print("不能除以0,异常:{} \n".format(e))
except ValueError as e:
	print("输入的是无效数字，异常:{}".format(e))


#多重异常捕获:
i =input("please input a number:")
n=666
try:
	result=n/int(i)
	print(result)
	print("{0} divided by {1} is {2}.".format(n,i,result))
except (ZeroDivisionError,ValueError) as e:
	print("异常发生:{} \n".format(e))


#嵌套(尽量不要使用)
i1 =input("please input a number:")
n=666

try:
	i2=int(i1)
	try:
		result=n/i2
		print("{0} divided by {1} is {2}.".format(n,i,result))
	except ZeroDivisionError as e1:
		print("不能除以0，异常e1：{}".format(e1))
except ValueError as e2:
	print("输入的是无效数字，异常e2：{0}".format(e2))


#finally 代码块释放资源
i =input("please input a number:")
n=666
try:
	result=n/int(i)
	print(result)
	print("{0} divided by {1} is {2}.".format(n,i,result))
except ZeroDivisionError as e:
	print("不能除以0,异常:{} \n".format(e))
except ValueError as e:
	print("输入的是无效数字，异常:{}".format(e))

finally:
	print("资源释放......\n")

#自定义异常类(需要继承exception类或其子类)
class ZhijieketangException(Exception):
	def __init__(self,message):    #构造方法，参数message是异常描述信息
		super().__init__(message)  #调用父类构造方法
		

#手动引发异常
class ZhijieketangException(Exception):
	def __init__(self,message):    
		super().__init__(message)  

i =input("please input a number:")
n=666
try:
	result=n/int(i)
	print(result)
	print("{0} divided by {1} is {2}.".format(n,i,result))
except ZeroDivisionError as e:
	# print("不能除以0,异常:{} \n".format(e))
	raise ZhijieketangException("不能除以零") 
except ValueError as e:
	# print("输入的是无效数字，异常:{}".format(e))
	raise ZhijieketangException("输入的是无效数字")
finally:
	print("\n资源释放......")

























































































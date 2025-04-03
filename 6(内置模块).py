#内置模块

#数学计算模块
import math

print(
math.ceil(2.4),
math.floor(2.4),
math.pow(5,3),
math.sqrt(2),
math.log(125,5),
math.degrees(0.5*math.pi),
math.radians(180),
math.sin(math.pi))  #默认为弧度制


#日期时间模块
import datetime
d=datetime.datetime(2023,8,1,12,13,10)
print(d)
d=datetime.datetime.today()
print(d)
d=datetime.datetime.now()
print(d)
d=datetime.datetime.fromtimestamp(1690885000.99)
print(d)

import datetime
d=datetime.date(2023,8,1)
print(d)
d=datetime.date.today()
print(d)
d=datetime.date.fromtimestamp(1690887000.00)
print(d)

import datetime
d=datetime.time(21,2,45,114514)
print(d)

#时间跨度
import datetime
d=datetime.date.today()
print(d)

delta=datetime.timedelta(10)  #默认更改对象为日期
d+=delta
print(d)

delta=datetime.timedelta(weeks=4)
d-=delta
print(d)
#或者有以下完全等价的代码:
delta=datetime.timedelta(weeks=-4)
d+=delta
print(d)

print('''
''')
#日期与字符串转换
import datetime

d=datetime.datetime.today()
print(type(d))

print(d.strftime("%Y-%m-%d %H:%M:%S"))
print(d.strftime("%Y-%m-%d"))
print(type(d.strftime("%Y-%m-%d")))

print('''
''')

str_date="2023-08-01 21:40:03"
print(type(str_date))

date=datetime.datetime.strptime(str_date,"%Y-%m-%d %H:%M:%S")
print(date)
print(type(date))

#strftime用于将日期对象转换为字符串
#strptime用于将字符串转换为日期对象(均有格式化参数format)




#正则表达式模块——re

#字符串匹配
import re
p=r"\w+@zhijieketang.com"  #注意为原始字符串,这说明什么?

email1=input("please input an email: ")
m=re.match(p,email1)
print(type(m))
print(m)
#若返回非空的Match对象,说明匹配成功
#将输出Match对象,span代表字符串跨度
if m==None:
	print("\n匹配失败，请确认输入的邮箱是否正确！")
else:
	print("\n匹配成功，欢迎进入系统！")


email2=input("\nplease input one more email: ")
m=re.match(p,email2)
print(type(m))
print(m)
#若返回None,说明匹配失败
if m==None:
	print("\n匹配失败，请确认输入的邮箱是否正确！")
else:
	print("\n匹配成功，欢迎进入系统！")



#字符串查找
import re 


p=r"\w+@zhijieketang\.com"  #正则表达式中|表示“或”
text="\nMy email is: "+input("\n请输入一个邮箱: ")

m=re.search(p,text)
print(m)
#search返回第一个查询到的对象


p=r"Java|java|JAVA"
text="I like Java and java and JAVA."

match_list=re.findall(p,text)
print("\n",match_list,"\n")
#findall返回所有查询到的对象


#字符串替换
import re 

p=r"\d+"    #匹配数字正则表达式,为什么该如此表达？
text="AB12CD34EF"

replace_text=re.sub(p," ",text)
print(replace_text)

replace_text=re.sub(p," ",text,count=1)
print(replace_text)

replace_text=re.sub(p," ",text,count=2)
print(replace_text)


#字符串分割

import re 

p=r"\d+"
text="AB12CD34EF"
print(text)

clist=re.split(p,text) #省略分割次数限制
print(clist)

clist=re.split(p,text,maxsplit=1)
print(clist)

clist=re.split(p,text,maxsplit=2)
print(clist)








































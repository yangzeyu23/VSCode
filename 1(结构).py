print("第一章节：")
for item in "hello!":
	print(item)

numbers =[1,2,3,4,5,6,7,8,9,10]
print("第二章节：")
for item in numbers :
	print(item)

print("第三章节：")
for item in range(100):
	if item==25:
		break
	print(item) #不知道为什么这一段语法是有效的




#for 语句测试
print("第一章节：")
for item in "hello!":
	print(item)

numbers =[1,2,3,4,5,6,7,8,9,10]
print("第二章节：")
for item in numbers :
	print(item)

print("第三章节：")
for item in range(10):
	if item==20:	
		break
	print(item)
else :
	print("the game is over.")      #in this situation the order "break" is harmfuless

for item in range(10):
	if item==2:
		continue
	print(item)
else:
	print("the game is over agaidn.")		


# while 语句测试
s=0
while s**2 <=100:
	s+=1

	print("s="+str(s))
	print("s**2="+str(s**2)) 
	print(str(s)+"**"+str(2)+"=",s**2)  #str 函数提供了将其他类型的数据转化为字符串的方法
else:
	print("the game is over.")

#题目：计算水仙花数
for s in range(101,1000):
	if s==(s%10)**3+((s%100-s%10)/10)**3+((s-(s%100))/100)**3:
		print("您好，为您找到的水仙花数有这几个："+str(s))
else:
	print("the task that was given by you has been finished already.")
#这段代码是成功运行的




#序列

#列表
a='internationalization'
print(a[1])
print(len(a))
print(max(a))
print(min(a))
b="gloabalization"
print(len(b))

list1=[34,23,12,145,111,222,2345,1,22,866,123]
list1+=[20]
print(list1)

list1[5]=11111
print(list1)

list1=[1,2,3,4,5,6,7,8,9,10]
list1.append(11)
print(list1)

t=[12,13,14,15]
list1.extend(t)
print(list1)

list1.insert(5,180)
print(list1)

list1.remove(180)
print(list1)
#切片操作：
g=[1,2,4,5,7,9,88,1003]  #[start:end:step]
print(g[0:7:2])


#元组
s_id,s_name=tuple([102,"Chenning Yang"])
print("the id is:"+str(s_id))               #再次注意此处需要使用str函数
print("the name is:"+s_name)

#集合
set1=set("internationalization")    
print(set1)
b={}
print(type(b))
s_set={"apple","banana","cat","dog"}   #集合的元素是无序的，不可重复的
s_set.add("egg")
print(s_set)

s_set.remove("banana")
print("下面开始查找集合中的某个元素：")
s=input("请输入待查找元素：")
if s in s_set:
	print("yes,we find the consequence for you.the set is considered to be:"+str(s_set))
else:
	print("the element is not given.")
# in / not in 均为判断函数
s_set.clear()
print(s_set)   #清除元素


#字典
dict1=dict({1: "apple",2: "banana",3: "cat",4: "dog",5: "elephant"})
print(dict1)
dict2=dict(zip([1,2,3,4,5],["a","b","c","d","e"])) #利用zip对元素进行打包
print(dict2)
print(dict2[4]) #查找

dict2[3]="z"    #更改
print(dict2)

dict2[6]="f"    #添加
print(dict2)

dict2.pop(6)
print(dict2)    #删除(key points)

#字典的访问
print(dict2.items())     #返回字典所有键值对视图
print(list(dict2.items()))

print(dict2.keys())      #返回字典键视图
print(list(dict2.keys()))

print(dict2.values())    #返回字典值视图
print(list(dict2.values()))

#遍历
#使用for 结构即可
print("以下为遍历结果：")

list2=[1,2,3,4,5]
for s in list2:
	print("数值"+str(s)+"为:"+str(s))

tuple1=tuple([1,2,3,4,5,6,7,8,9,10])
print(tuple1)
for i in tuple1:
	if i>=8:
		break
	print("元素"+str(i)+"为："+str(i))

set2={11,22,33,44,55,66,77,88,99,100} #注意集合无序
print("the elements include:")
for u in set2:
	print(u)


dict3=dict(zip([1,2,3,4,5],["a","b","c","d","e"]))
for i,j in dict3.items():
	print("学号：{0}-学生：{1}".format(i,j))
#format函数可以提供自动编号

for r in dict3.keys():
	print("学号为："+str(r))
for w in dict3.values():
	print("姓名为："+w)   
	#注意此处不需使用str函数，因为本就是字符串








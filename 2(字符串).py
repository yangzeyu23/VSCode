#字符串

s="the space tell the substance how to move.\nthe substance tell the space how to curve. "
print(s)
s="space\tsubstance"
print(s)
s="inter\"good"
print(s)
s='inter\'good'
print(s)
s="inter\\inter"
print(s)

#原始字符串
e=r"the space.\\he suctance."
print(e)
e="the space.\\the suctance."
print(e)

#长字符串
s='''
the winner.
the danger.
the power.
the poker.
'''
print(s)

#转数字
print(int("123444"))
print(float("123444"))
print(int("EFF",16))
#转字符串
assessment=114514
print(str(assessment))

#格式化
r="best"
s="student{p1} is the {p2} children {p3} have ever seen.".format(p1=1,p2=r,p3="I")
print(s)

print('''



————————以下为一个自幂运算器：————————''')
w=input("请输入一个正整数：")
s="{p1}**{p1}={p2}".format(p1=w,p2=int(w)**int(w)) #w要化为数字形式
print(s)
print('''——————————————~运算结束~——————————————



	''')

#格式化控制符
number=1
name="Andy"
age=17
score=114514
s="学生{0:d},{1:s},年龄为:{2:d}，他的期末考试成绩为:{3:f}".format(number,name,age,score)
print(s)

g="十进制数字{0:d}的十六进制表示为：{0:x}".format(100)
print(g)

s="学生{0:d}的绩点为:{1:E}.".format(1,114514)
print(s)


#字符串查找
s="internationalization"
print(s.find("o",1,7))   #返回-1即未查找到

#字符串替换
s="AB CD EF GH IJ KL"
print(s.replace(" ","|",4))
print(s.replace(" ","|"))  #不指定数量默认为对于全部操作

#字符串分割
s="AB CD EF GH IJ KL"
print(s.split(" ",maxsplit=3))


#计算文本单词频率
wordstring='''
	it was the best of times it was the worst of times.
	it was the age of wisdom it was the age of foolishness.
'''  
wordstring=wordstring.replace("."," ")
wordlist=wordstring.split()

wordfreq=[]

for w in wordlist:
	wordfreq.append(wordlist.count(w))

d=dict(zip(wordlist,wordfreq))
print(d)




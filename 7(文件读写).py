#文件读写

#打开文件
f=open("新建 DOCX 文档 (3).docx","w+")
f.write("World")
print("创建新建 DOCX 文档 (3).docx文件，Word写入文件")


f=open("新建 DOCX 文档 (3).docx","r+")
f.write("Hello,")
print("打开新建 DOCX 文档 (3).docx文件，Hello覆盖属性内容")


f=open("新建 DOCX 文档 (3).docx","a")
f.write(" ")
print("打开新建 DOCX 文档 (3).docx文件，在文件尾部追加空格")


fname='C:/Users/25302/Desktop/新建 DOCX 文档 (3).docx'
#还有两种表达方式:
#fname=r"C:\Users\25302\Desktop\新建 DOCX 文档 (2).docx"
#fname="C:\\Users\\25302\\Desktop\\新建 DOCX 文档 (2).docx"
#注意斜杠的方向
f=open("新建 DOCX 文档 (3).docx","a+")
f.write("world!")
print("打开新建 DOCX 文档 (3).docx文件，在文件尾部追加world")

#注意:我的输出结果与示例文档结果不一样,注意回头检查以一下出现了什么异常


#关闭文件

#finally代码块
f_name="新建 DOCX 文档 (3).docx"
f=None

try:
	f=open(f_name)       #可能引发FileNotFoundError
	print("打开文件成功!")
	content=f.read()     #可能引发OSError异常
	print(content)
except FileNotFoundError as e:
	print("文件不存在，请先使用 7(文件读写).py程序创建文件.")
except OSError as e:
	print("处理OSE异常")
finally:
	if f is not None:    #判断变量是否有数据，如果文件有数据，则说明文件打开成功
		f.close()        #关闭文件
		print("关闭文件成功！")
	else:
		print("文件在操作之前已经正常关闭。")


#优化:with as 代码块
f_name="新建 DOCX 文档 (3).docx"
with open(f_name) as f:
	content=f.read()
	print("\n"+content)
#在as后已经声明了一个资源变量，代码块结束后会自动释放资源


#复制文本文件
f_name="新建 DOCX 文档 (3).docx"
with open(f_name,"r",encoding="gbk") as f:
	lines=f.readlines()

	copy_f_name="新建 DOCX 文档 (4).docx"
	with open(copy_f_name,"w",encoding='utf-8') as copy_f:
		copy_f.writelines(lines)
		print("\n文件复制成功!")

#复制二进制文件
f_name="C:/Users/25302/Pictures/Saved Pictures/fox.jpg"

with open(f_name,"rb") as f:
	b=f.read()
	copy_f_name="C:/Users/25302/Pictures/Saved Pictures/fox2.jpg"
	with open(copy_f_name,"wb") as copy_f:
		copy_f.write(b)
		print("\n文件复制成功！")

#最后强调一些知识:
# r & r+: 通过r只能读数据，r+可以读写数据
# w & w+: 通过w只能写数据，w+可以读写数据
# a & a+: 通过a只能写数据(追加)，w+可以读写数据

#文本文件:   GBK, UTF-8
#二进制文件: jpg, png, exe, Word, Excel, PPT










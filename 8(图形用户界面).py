#图形使用界面

#下载wxPython

#创建应用对象和窗口对象
import wx 

#创建应用程序对象
app=wx.App()

#创建窗口对象
frm=wx.Frame(None,title="第一个wxPython程序!",size=(400,300),pos=(100,100))
#规定窗口的大小,位置

#显示窗口(默认隐藏,需要调用方可显示)
frm.Show()

#进入主事件循环
app.MainLoop()





import wx 

#自定义窗口类
class MyFrame(wx.Frame):
	def __int__(self):
		super().__int__(None,title="第一个wxPython程序!",size=(400,300),pos=(100,100))

app=wx.App()

frm=MyFrame()
frm.Show()

app.MainLoop()



#创建面板和静态文本
import wx

class MyFrame(wx.Frame):
	def __int__(self):
		super().__int__(None,title="第一个wxPython程序!",size=(400,300),pos=(100,100))
		panel=wx.Panel(parent=self)
		statictext=wx.StaticText(parent=panel,label="Hello,World!",pos=(10,10))
		#lable是静态文本对象上显示的文字

app=wx.App()

frm=MyFrame()
frm.Show()

app.MainLoop()

#因为IDLE是用Tkinker开发的，它会和wxWidget的mainloop()冲突

#事件响应
import wx

class MyFrame(wx.Frame):
	def __int__(self):
		super().__int__(None,title="事件处理",size=(300,100))
		panel=wx.Panel(parent=self)
		self.statictext=wx.StaticText(parent=panel,label="请单击OK按钮",pos=(110,20))
		b=wx.Button(parent=panel,label="OK",pos=(100,50))
		#创建按钮对象
		self.Bind(wx.EVT_BUTTON,self.on_click,b)
		#绑定事件

	def on_click(self,event):
	#事件处理程序
		self.statictext.SetLabelText("Hello,World!")

app=wx.App()

frm=MyFrame()
frm.Show()

app.MainLoop()




#布局管理

#盒子布局管理器
import wx

class MyFrame(wx.Frame):
	def __int__(self):
		super().__int__(None,title="事件处理",size=(300,180))
		panel=wx.Panel(parent=self)
		self.statictext=wx.StaticText(parent=panel,label="请单击OK按钮")
		b=wx.Button(parent=panel,label="OK")
		self.Bind(wx.EVT_BUTTON,self.on_click,b)

		vbox=wx.BoxSizer(wx.VERTICAL)
		vbox.Add(self.statictext,proportion=1,
			flag=wx.ALIGIN_CENTER_HORIZONAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
		vbox.Add(b,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)
		panel.SetSizer(vbox)

	def on_click(self,event):
		self.statictext.SetLabelText("Hello,World!")

app=wx.App()
frm=MyFrame()
frm.Show()
app.MainLoop()


#还有很多控件,未完待续。








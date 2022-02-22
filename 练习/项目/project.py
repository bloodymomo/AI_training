# coding =untf-8

# f_name = 'src_tt.txt'

# with open(f_name, 'r', encoding = 'utf-8') as f:
#     lines = f.readlines()
#     copyFName = 'src_copy.txt'
#     with open(copyFName,'w',encoding='utf-8') as copyF:
#         copyF.writelines(lines)
#         print('复制成功')

#二进制
# f_name = 'test.jpg'

# with open(f_name, 'rb') as f:
#     lines = f.read()
#     copyFName = 'copy.jpg'
#     with open(copyFName,'wb') as copyF:
#         copyF.write(lines)
#         print('复制成功')

#from tkinter import VERTICAL
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title = '布局器嵌套', size= (300,120))# pos =(100,100))
        panel = wx.Panel(parent= self)
        self.statc = wx.StaticText(parent = panel, label = "请单击按钮", pos = (10,10))
        b1=wx.Button(parent = panel,id =10, label = 'Button 1') #10,11是按钮ID
        b2=wx.Button(parent = panel, id =11, label = 'Button 2')
        
        
        #定义布局器
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        #添加statc布局器(占比，控件flag位置，边框)

        #添加b布局器(占比，控件flag位置，边框)
        hbox.Add(b1, proportion =1,flag = wx.EXPAND | wx.ALL, border = 10)
        hbox.Add(b2, proportion =1,flag = wx.EXPAND | wx.ALL, border = 10)
        #设置面板（panel）采用vbox布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statc, proportion =1,flag = wx.ALIGN_CENTER_HORIZONTAL
        | wx.FIXED_MINSIZE | wx.TOP, border = 30)
        #hbox布局器对象到vbox布局器对象
        vbox.Add(hbox,proportion = 1, flag=wx.CENTER)
        #采用vbox布局
        panel.SetSizer(vbox)
        #将b1,b2单击绑定到self.on_click上
        self.Bind(wx.EVT_BUTTON,self.on_click,id = 10,id2=20)

    def on_click(self, event):
        event_id = event.GetId()#获得ID
        print(event_id)
        #根据ID判断单击了哪个按钮
        if event_id ==10:
            self.statc.SetLabelText("Button1单击")
        else:
            self.statc.SetLabelText("Button2单击")


#frm = wx.Frame(None,title = "first", size=(400,300), pos = (100,100))
app= wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()
print(dir(app))

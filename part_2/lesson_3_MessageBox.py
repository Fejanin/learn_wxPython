import wx
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
 
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap((r'img\target.png')))
        toolbar.Realize()
 
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
 
    def onQuit(self, e):
        dlg = wx.MessageBox('Вы дейстительно хотите выйти из программы?', 'Вопрос',
			wx.YES_NO | wx.NO_DEFAULT, self)
        print(dlg)
        if dlg == wx.YES:
            print("Нажата кнопка (да)")
        elif dlg == wx.NO: 
            print("Нажата кнопка (нет)")
 
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

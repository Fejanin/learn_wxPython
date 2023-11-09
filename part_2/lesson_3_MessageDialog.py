import wx
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
 
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap((r'img\target.png')))
        toolbar.Realize()
 
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
 
    def onQuit(self, e):
        dlg = wx.MessageDialog(self, 'Вы дейстительно хотите выйти из программы?', 'Вопрос',
             wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        res = dlg.ShowModal()
        print(res)
        if res == wx.ID_YES:
            print("Нажата кнопка (да)")
        elif res == wx.ID_NO:
            print("Нажата кнопка (нет)")


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

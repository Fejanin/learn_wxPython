import wx
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
 
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap((r'img\target.png')))
        toolbar.Realize()
 
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
 
    def onQuit(self, e):
        dlg = wx.DirDialog(self, "Выбор директории...", "D:",
         wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
 
        res = dlg.ShowModal()
        print(dlg, res)
        if res == wx.ID_OK:
            print("Выбран каталог: "+dlg.GetPath())
 
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

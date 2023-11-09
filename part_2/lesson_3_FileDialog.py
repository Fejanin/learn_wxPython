import wx
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
 
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap((r'img\target.png')))
        toolbar.Realize()
 
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
 
    def onQuit(self, e):
        with wx.FileDialog(self, "Открыть файл...", wildcard="Файлы Питона (*.py)|*.py", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
              if fileDialog.ShowModal() == wx.ID_CANCEL:
                   return 
         
              pathname = fileDialog.GetPath()
              print(pathname)
 
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

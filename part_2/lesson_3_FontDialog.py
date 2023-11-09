import wx
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
 
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap((r'img\target.png')))
        toolbar.Realize()
 
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
 
    def onQuit(self, e):
        dlg = wx.FontDialog(self)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            font = dlg.GetFontData().GetChosenFont() #wx.Font
            print(font.GetFaceName())
 
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

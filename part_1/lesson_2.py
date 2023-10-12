import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)


class MyFrame1(wx.MDIParentFrame ):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)
        win = wx.MDIChildFrame(self, -1, "Child Window", size=(200, 150))
        win.Show()


app = wx.App()
 
wnd = MyFrame1(None, "Hello World!")
wnd.Show()
app.MainLoop()

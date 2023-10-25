import wx
 
class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600,300))

        t1 = wx.TextCtrl(self)
        t2 = wx.TextCtrl(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(t1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(t2, flag=wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(vbox)

        t1.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        t1.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
 
        t2.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        t2.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnSetFocus(self, event):
        event.GetEventObject().SetBackgroundColour("#FFFFE5")
        event.Skip()
 
    def OnKillFocus(self, event):
        event.GetEventObject().SetBackgroundColour("#fff")
        event.Skip()

        
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

import wx
 
class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600,300))
 
        self.x = wx.StaticText(self, label='x:', pos=(10, 10))
        self.y = wx.StaticText(self, label='y:', pos=(10, 30))
 
        self.Bind(wx.EVT_MOTION, self.OnMove)
        self.Bind(wx.EVT_PAINT, self.OnPaint)


    def OnMove(self, event):
        x, y = event.GetPosition()
        self.x.SetLabel('x: ' + str(x))
        self.y.SetLabel('y: ' + str(y))

    def OnPaint(self, event):
        print("событие EVT_PAINT")
        dc = wx.PaintDC(self)
        dc.DrawLine(0,0, 100, 100)

        
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

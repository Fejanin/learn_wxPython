import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size=(800, 700)):
        super().__init__(parent, title=title, size=size)

        panel = wx.Panel(self)

        img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("img/robo_1.jpg"))
        img2 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("img/robo_2.jpg"))

        #img1.SetPosition((10, 10))
        #img2.SetPosition((400, 40))

        vbox = wx.BoxSizer() # (wx.VERTICAL)
        vbox.Add(img1, wx.ID_ANY, wx.EXPAND)
        vbox.Add(img2, wx.ID_ANY, wx.EXPAND)

        #mp = wx.Panel(panel)
        #mp.SetBackgroundColour('#FFFFE5')
        #vbox.Add(mp, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        panel.SetSizer(vbox)


app = wx.App()
 
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()

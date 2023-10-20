import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)

        gr = wx.GridBagSizer(5, 5)
        text = wx.StaticText(panel, label="Email:")
        gr.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        tc = wx.TextCtrl(panel)
        gr.Add(tc, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        button1 = wx.Button(panel, label='Восстановить', size=(120, 28))
        button2 = wx.Button(panel, label='Отмена', size=(90, 28))

        gr.Add(button1, pos=(3, 3))
        gr.Add(button2, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=10)

        gr.AddGrowableCol(1)
        gr.AddGrowableRow(2)
        
        panel.SetSizer(gr)


app = wx.App()
 
wnd = MyFrame(None, "GridBagSizer")
wnd.Show()
app.MainLoop()

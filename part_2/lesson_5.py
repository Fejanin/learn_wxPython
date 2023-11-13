import wx

B_RED = 1
B_GREEN = 2
B_BLUE = 3
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 450))
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Текст в статусной строке")

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vbox)

        st = wx.StaticText(panel, label="Адрес: ")
        vbox.Add(st, flag=wx.ALL, border=10)

        inp = wx.TextCtrl(panel, value="введите адрес")
        vbox.Add(inp, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        rtb = wx.ToggleButton(panel, id = B_RED, label='red', pos=(20, 25))
        gtb = wx.ToggleButton(panel, id = B_GREEN, label='green', pos=(20, 60))
        btb = wx.ToggleButton(panel, id = B_BLUE, label='blue', pos=(20, 100))
        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        self.col = wx.Colour(0, 0, 0)
        self.pn = wx.Panel(panel)
        self.pn.SetBackgroundColour(self.col.GetAsString())
        vb1 = wx.GridBagSizer(10, 10)
        vb1.Add(rtb, (0, 0)); vb1.Add(gtb, (1, 0)); vb1.Add(btb, (2, 0))
        vb1.Add(self.pn, (0, 1), (3, 1), flag=wx.EXPAND)
        vb1.AddGrowableCol(1)
        vbox.Add(vb1, flag=wx.EXPAND|wx.ALL, border=10)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        pn2 = wx.Panel(panel)
        wx.StaticBox(pn2, label="Ваш пол:", size=(150, 50))
        rd1 = wx.RadioButton(pn2, label="Муж", pos=(10, 20), style=wx.RB_GROUP)
        rd2 = wx.RadioButton(pn2, label="Жен", pos=(100, 20))
        vb2 = wx.BoxSizer(wx.HORIZONTAL)
        vb2.Add(pn2)
        links = ["Телефон", "E-mail", "Skype"]
        cb = wx.ComboBox(panel, pos=(50, 30), choices=links, style=wx.CB_READONLY)
        cb.SetSelection(0)
        sc = wx.SpinCtrl(panel, value='0', min=-100, max=100)
        vb2.Add(cb, flag=wx.LEFT | wx.TOP, border=15)
        vb2.Add(sc, flag=wx.LEFT | wx.TOP, border=15)
        vbox.Add(vb2, flag=wx.EXPAND | wx.ALL, border=10)

        self.gauge = wx.Gauge(panel, range=100)
        vbox.Add(self.gauge, flag=wx.EXPAND|wx.ALL, border=10)

        bStart = wx.Button(panel, label="Старт")
        bStop = wx.Button(panel, label="Стоп")
        bStart.Bind(wx.EVT_BUTTON, self.onStart)
        bStop.Bind(wx.EVT_BUTTON, self.onStop)
        hb3 = wx.BoxSizer()
        hb3.AddMany([(bStart, 0, wx.LEFT|wx.RIGHT, 10), (bStop, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 10)])
        vbox.Add(hb3, flag=wx.ALIGN_CENTRE)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.count = 0
        self.gauge.SetValue(self.count)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        sld = wx.Slider(panel, value=200, minValue=150, maxValue=500, style=wx.SL_HORIZONTAL)
        sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        vbox.Add(sld, flag=wx.EXPAND|wx.ALL, border=10)

    def onToggle(self, e):
        btn = e.GetEventObject()
        val = 255 if btn.GetValue() else 0
        id = btn.GetId()
 
        r = self.col.Red()
        g = self.col.Green()
        b = self.col.Blue()
 
        if id == B_RED:
            self.col.Set(val, g, b)
        elif id == B_BLUE:
            self.col.Set(r, g, val)
        elif id == B_GREEN:
            self.col.Set(r, val, b)
 
        self.pn.SetBackgroundColour(self.col)
        self.pn.Refresh()

    def OnTimer(self, e):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)
 
        if self.count >= 100:
            self.timer.Stop()

    def onStop(self, e):
        self.timer.Stop()
        self.count = 0
 
    def onStart(self, e):
        if self.count > 100:
            return
 
        self.timer.Start(100)

    def OnSliderScroll(self, e):
        val = e.GetEventObject().GetValue()
        self.sb.SetStatusText("Slider: "+str(val))

 
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

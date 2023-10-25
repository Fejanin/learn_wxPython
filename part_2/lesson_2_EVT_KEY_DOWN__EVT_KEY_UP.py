import wx

BUTTON1 = wx.NewIdRef() # присиваем уникальные id
BUTTON2 = wx.NewIdRef() # присиваем уникальные id

class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600,300))

        b1 = wx.Button(self, BUTTON1.GetId(), label="Кнопка 1")
        b2 = wx.Button(self, BUTTON2.GetId(), label="Кнопка 2")
 
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(b2, flag=wx.EXPAND | wx.ALL, border=10)
 
        self.SetSizer(vbox)

        # отслеживает нажатие клавиш клавиатуры
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
 
    def OnKeyDown(self, e):
        print("Нажали кнопку")
        key = e.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Вы дейстительно хотите выйти из программы?', 'Вопрос', 
                                wx.YES_NO | wx.NO_DEFAULT, self)
 
            if ret == wx.YES:
                self.Close()
 
    def OnKeyUp(self, e):
        print("Отпустили кнопку")


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

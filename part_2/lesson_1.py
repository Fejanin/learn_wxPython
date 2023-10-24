import wx
 
class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600,300))
        panel = wx.Panel(self)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow) # только self, чтобы закрыть основное окно
        
        panel.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)

        btn1 = wx.Button(panel, wx.ID_ANY, "Кнопка 1")
        btn2 = wx.Button(panel, wx.ID_ANY, "Кнопка 2")
        btn1.SetPosition(wx.Point(10, 10))
        btn2.SetPosition(wx.Point(200, 10))

        self.Bind(wx.EVT_BUTTON, self.onButton1, btn1)
        self.Bind(wx.EVT_BUTTON, self.onButton2, btn2)
                
        
        btn = wx.Button(panel, wx.ID_ANY, "Нажать")
        btn.SetPosition(wx.Point(200, 100))
        
        btn.Bind(wx.EVT_BUTTON, self.onButton, btn)
        panel.Bind(wx.EVT_BUTTON, self.onButtonPanel, btn)
        self.Bind(wx.EVT_BUTTON, self.onButtonFrame, btn)

    def onLeftDown(self, event):
        print("Нажатие на левую кнопку мыши")

    def onButton1(self, event):
        print("Нажатие на кнопку 1")

    def onButton2(self, event):
        print("Нажатие на кнопку 2")

    def onButton(self, event):
        print("Уровень кнопки")
        event.Skip() # перебрасывает событие на следующий уровень
 
    def onButtonPanel(self, event):
        print("Уровень панели")
        event.Skip() # перебрасывает событие на следующий уровень
 
    def onButtonFrame(self, event):
        print("Уровень окна")

    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(None, 'Вы действительно хотите выйти?', 'Вопрос',  
                     wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
 
        ret = dial.ShowModal()
 
        if ret == wx.ID_YES:
            self.Destroy() # уничтожить окно, использовать Close() нельзя, иначе снова будет вызвана ф-ция OnCloseWindow
        else:
            event.Veto() # прерывает дальнейшую обработку данного события
        
 
app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

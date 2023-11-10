import wx


class MyDlg(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetSize(500, 150)
 
        vb = wx.BoxSizer(wx.VERTICAL)
        vb.Add(wx.TextCtrl(self, wx.ID_ANY), flag=wx.EXPAND | wx.ALL, border=10)
 
        vh = wx.BoxSizer(wx.HORIZONTAL)
        bOk = wx.Button(self, wx.ID_OK, label="Да", size=(100, 30))
        bCn = wx.Button(self, wx.ID_CANCEL, label="Отмена", size=(100, 30))
        vh.Add(bOk, flag=wx.LEFT, border = 10)
        vh.Add(bCn, flag=wx.LEFT, border=10)
 
        vb.Add(vh, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        self.SetSizer(vb)

        bOk.Bind(wx.EVT_BUTTON, self.onOk)

    def onOk(self, event): 
        self.EndModal(wx.ID_OK)


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
 
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap(r'img\target.png'))
        toolbar.AddSeparator()
        dialog = toolbar.AddTool(wx.ID_ANY, "Диалог", wx.Bitmap(r'img\num_1.png'))
        toolbar.Realize()
 
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
        self.Bind(wx.EVT_TOOL, self.onDialog, dialog)

    def onDialog(self, e):
        dlg = MyDlg(self, title="Мой диалог...")
        res = dlg.ShowModal() # создаем модальное окно, для создания не модального - dlg.Show() и удалить - dlg.Destroy()
        dlg.Destroy()
        print(res)
        if res == wx.ID_OK:
            print("Нажата кнопка да")
 
    def onQuit(self, e):
        self.Close()



app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

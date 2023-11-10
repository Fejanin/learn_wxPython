import wx


class MyDlg(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
 
    def onQuit(self, e):
        self.Close()


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()

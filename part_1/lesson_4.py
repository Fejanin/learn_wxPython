import wx


APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4


class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
 
        it_min = self.Append(wx.ID_ANY, "Минимизировать")
        it_max = self.Append(wx.ID_ANY, "Распахнуть")
        self.Bind(wx.EVT_MENU, self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU, self.onMaximize, it_max)
 
    def onMinimize(self, event):
        self.parent.Iconize()
 
    def onMaximize(self, event):
        self.parent.Maximize()


class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)
 
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
 
        item = wx.MenuItem(fileMenu, APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap(r'img\target.png'))
        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        fileMenu.AppendSeparator()
        expMenu = wx.Menu()
        expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        expMenu.Append(wx.ID_ANY, "Экспорт видео")
        expMenu.Append(wx.ID_ANY, "Экспорт данных")
        fileMenu.AppendSubMenu(expMenu, "&Экспорт")
        fileMenu.Append(item)

        viewMenu = wx.Menu()
        self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)
        
        menubar.Append(fileMenu, "&File")
        menubar.Append(viewMenu, "&Вид")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        #toolbar = self.CreateToolBar()
        #toolbar = self.CreateToolBar(wx.TB_RIGHT)
        #toolbar = self.CreateToolBar(wx.TB_LEFT)
        toolbar = self.CreateToolBar(wx.TB_BOTTOM)
        
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap(r'img\target.png'))
        toolbar.AddSeparator()
        br_undo = toolbar.AddTool(wx.ID_UNDO, "", wx.Bitmap(r"img\arrow_right.png"))
        br_redo = toolbar.AddTool(wx.ID_REDO, "", wx.Bitmap(r"img\arrow_left.png"))

        toolbar.EnableTool(wx.ID_REDO, False) # делает виджет неактивным
        
        toolbar.AddSeparator()
        toolbar.AddCheckTool(wx.ID_ANY, "", wx.Bitmap(r'img\num_1.png'))
        toolbar.AddRadioTool(wx.ID_ANY, "", wx.Bitmap(r'img\num_2.png'))
        toolbar.AddRadioTool(wx.ID_ANY, "", wx.Bitmap(r'img\num_3.png'))
        
        toolbar.Realize() # для Windows

        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
        

    def OnRightDown(self, event):
        self.ctx = AppContextMenu(self)
        self.PopupMenu(self.ctx, event.GetPosition())


    def onQuit(self, event):
        self.Close()

    def onStatus(self, event):
        if self.vStatus.IsChecked():
           print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")
 
    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print("Режим RGB")
        elif self.vSrgb.IsChecked():
            print("Режим sRGB")

app = wx.App()
frame = MyFrame(None, 'Hello world!')
frame.Show()

app.MainLoop()

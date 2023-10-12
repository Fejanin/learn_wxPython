import wx


app = wx.App() # класс общего функционала приложения

frame = wx.Frame(None, wx.ID_ANY, title='Hello world!') # класс отдельного окна (их может быть несколько)
frame.Show()
# В конструкторе класса Frame мы указываем три параметра:
# parent – ссылка на родительское окно (если его нет, то указывается None, тогда окно становится главным окном приложения);
# id – уникальный идентификатор виджета (указывая wx.ID_ANY мы говорим, чтобы он формировался автоматически);
# title – заголовок окна.
# Конечно, конструктор класса Frame содержит и другие параметры, полный синтаксис следующий:
# wx.Frame(parent, id=-1, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="frame")
# Названия параметров говорят сами за себя, единственно, что следует подробнее расшифровать – это параметр DEFAULT_FRAME_STYLE, который состоит из набора следующих констант:
# wx.DEFAULT_FRAME_STYLE = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
# Здесь вот эта вертикальная черта – операция побитового ИЛИ, с помощью которой и происходит объединение всех этих свойств. А сами свойства означают следующее:
# wx.MINIMIZE_BOX – кнопка для свертывания окна;
# wx.MAXIMIZE_BOX – кнопка для распахивания окна;
# wx.CLOSE_BOX – кнопка закрытия окна;
# wx.RESIZE_BORDER – делаем окно с изменяемым размером;
# wx.SYSTEM_MENU – разрешаем системное меню;
# wx.CAPTION – разрешаем заголовок у окна.
# ПРИМЕРЫ:
# wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(200, 200))
# wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(500, 200), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
# wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(500, 200), pos = (100,0))
wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(500, 200))
wnd.Centre()
wnd.Maximize()
# Получим окно по центру. Также доступны такие полезные методы класса Frame:
# Close() – закрывает окно;
# Maximize() – распахивает окно на весь экран;
# Move(x, y) – располагает окно со смещением x, y пикселей от верхнего левого угла экрана;
# SetPosition( pt: wx.Point ) – помещает окно с начальной точкой pt, например, wnd.SetPosition( wx.Point(100, 500) );
# SetSize(x, y, width, height) – устанавливает положение и размер окна.

wnd.Show()

app.MainLoop()

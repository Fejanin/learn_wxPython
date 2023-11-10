На этом занятии продолжим тему диалоговых окон и посмотрим как можно создавать свои собственные диалоги. Это делается очень просто. 
Все диалоговые окна наследуются от класса Dialog, имеющий следующий синтаксис:

wx.Dialog(parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr)

parent – ссылка на родительское окно (или значение None);
id – идентификатор окна;
title – заголовок окна;
pos, size – позиция и размер окна;
style – стилизация окна.

wx.CAPTION – разрешает заголовок окна;
wx.DEFAULT_DIALOG_STYLE (комбинация констант: wx.CAPTION, wx.CLOSE_BOX и wx.SYSTEM_MENU);
wx.RESIZE_BORDER – разрешает изменять размеры окна;
wx.SYSTEM_MENU – для отображения системного меню;
wx.CLOSE_BOX – для отображения кнопки закрытия (с крестиком);
wx.MAXIMIZE_BOX – для возможности распахивания окна;
wx.MINIMIZE_BOX – для возможности свертывания окна;
wx.STAY_ON_TOP – для отображения окна поверх всех остальных.
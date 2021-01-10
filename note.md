- qt控件，控制可随窗口大小伸缩
https://blog.csdn.net/qq_44957388/article/details/105925404


安装太慢， 使用豆瓣源
```bash
pip install PyQt5 -i https://pypi.douban.com/simple
```


xlrd读取文件，注意事项：
- 读取之前记得先关闭筛选等一下乱七八糟的设置，避免读取的时候失败

dialog、widget、mainwindow的区别  
    1. dialog有exec函数，如果是dialog窗口，后边的窗口时不可选的；
    2. widget和dialog都有show函数，如果通过这个函数显示这两种类型的窗口，则两个窗口都是可选的；
    3. widget主要是在上面放置布局和控件；
    4. mainwindow可以显示菜单，工具栏，状态栏、托盘等功能。


![image:]https://doc.qt.io/qt-5/images/qtableview-resized.png
	By default, the cells in a table do not expand to fill the available space.
You can make the cells fill the available space by stretching the last header section. Access the relevant header using horizontalHeader() or verticalHeader() and set the header's stretchLastSection property.

To distribute the available space according to the space requirement of each column or row, call the view's resizeColumnsToContents() or resizeRowsToContents() functions.


- Error in input file: not well-formed (invalid token): 
- This error popped because my .ui file was not saved with the recent changes that i had done. The file name showed the asterisk(*) mark in the file name. Once i saved the file with changes it could be converted into a .py file.
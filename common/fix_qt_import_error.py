# coding: utf-8
# @Time    : 2019/10/28 10:23
# @Author  : 蟹蟹 ！！
# @FileName: 22.py
# @Software: PyCharm

# Fix qt import error
# Include this file before import PyQt5
import os
import sys


def _append_run_path():
    if getattr(sys, 'frozen', False):
        pathlist = []

        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        pathlist.append(sys._MEIPASS)

        # the application exe path
        _main_app_path = os.path.dirname(sys.executable)
        pathlist.append(_main_app_path)

        # append to system path enviroment
        os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)

_append_run_path()
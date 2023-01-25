# [PyQt6](https://www.riverbankcomputing.com/software/pyqt/intro)

Is a set of [[python]] bindings for The Qt Company's Qt application framework that allow us to create [[graphical user interface|GUIs]] using [[css|CSS]] to style the widgets. 
It runs on all platforms supported by Qt including Windows, macOS, Linux, iOS and Android.

## [Documantation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)

- [Modules](https://doc.qt.io/qtforpython-5/modules.html) is a list of all the modules in PyQt6.

## Main Classes

### QMainWindow

Provides the main applicatioon Window. It is the top level window that contains the menu bar, toolbars, status bar and central widget.

### QDialog

Is the base class of dialog windows. It provides a dialog frame with a top level window mostly used shortly for short-term tasks and brief communications with the user.

### [QWidget](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/index.html#module-PySide2.QtWidgets)

Is the base class of all the UI objects. The widget is the important poinr of the UI, it provides mouse, keyboard and events from the window system, and it can draw itself on the screen.

### \*.ui to \*.py
The way to convert a .ui file created by the QtDesigner to an actual python file is using the `pyui6` command.
```bash
pyui6 -x <file.ui> -o <file.py>
```

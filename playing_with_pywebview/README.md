Started:

https://www.techiediaries.com/python/how-to-build-cross-platform-desktop-gui-based-apps-with-python-and-web-technologies-and-frameworks/



Did not spend a lot of time getting to work.


```
$ python intro.py 
ERROR:webview:GTK cannot be loaded
Traceback (most recent call last):
  File "/home/dstoner/git/Envs/python_experiments/local/lib/python2.7/site-packages/webview/__init__.py", line 73, in _initialize_imports
    import webview.gtk as gui
  File "/home/dstoner/git/Envs/python_experiments/local/lib/python2.7/site-packages/webview/gtk.py", line 14, in <module>
    import gi
ImportError: No module named gi
WARNING:webview.qt:PyQt4 is not found
ERROR:webview.qt:PyQt5 is not found
Traceback (most recent call last):
  File "/home/dstoner/git/Envs/python_experiments/local/lib/python2.7/site-packages/webview/qt.py", line 36, in <module>
    from PyQt5 import QtCore
ImportError: No module named PyQt5
Traceback (most recent call last):
  File "intro.py", line 2, in <module>
    webview.create_window("Techiediaries", "http://www.techiediaries.com",width=800, height=600, resizable=True, fullscreen=False) 
  File "/home/dstoner/git/Envs/python_experiments/local/lib/python2.7/site-packages/webview/__init__.py", line 178, in create_window
    _initialize_imports()
  File "/home/dstoner/git/Envs/python_experiments/local/lib/python2.7/site-packages/webview/__init__.py", line 82, in _initialize_imports
    import webview.qt as gui
  File "/home/dstoner/git/Envs/python_experiments/local/lib/python2.7/site-packages/webview/qt.py", line 56, in <module>
    raise Exception("This module requires PyQt4 or PyQt5 to work under Linux.")
Exception: This module requires PyQt4 or PyQt5 to work under Linux.

```

Possible help...

http://movingthelamppost.com/blog/html/2013/07/12/installing_pyqt____because_it_s_too_good_for_pip_or_easy_install_.html

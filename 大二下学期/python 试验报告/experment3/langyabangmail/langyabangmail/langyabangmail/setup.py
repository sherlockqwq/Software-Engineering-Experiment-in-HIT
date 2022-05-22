



from distutils.core import setup
import py2exe
import sys
import PyQt5
from PyQt5 import QtWebEngineWidgets
import glob

sys.argv.append('py2exe')

py2exe_options = {
        "includes": ["sip","PyQt5.QtGui","PyQt5.QtWidgets","PyQt5.QtCore",
                    "PyQt5.QtWebEngineWidgets","PyQt5.QtWebEngine","PyQt5.QtNetwork",
                    "PyQt5.QtNetwork","PyQt5.QtPrintSupport"],  # 如果打包文件中有PyQt代码，则这句为必须添加的
        "dll_excludes": ["MSVCP90.dll",
                  "MSWSOCK.dll",
                  "mswsock.dll",
                  "powrprof.dll",],  # 这句必须有，不然打包后的程序运行时会报找不到MSVCP90.dll，如果打包过程中找不到这个文件，请安装相应的库
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 3, 
      #  "bundle_files": 1,  # 关于这个参数请看第三部分中的问题(2)
        }

setup(
      name = 'PyQt Demo',
      version = '1.0',
      windows=[{"script": "pxmail.py", "icon_resources": [(1, "icon.ico")] }],   # 括号中更改为你要打包的代码文件名
       data_files=[("",
                    [r"D:\python3.4\Lib\site-packages\PyQt5\libEGL.dll"]),
                   ("platforms",
                    [r"D:\python3.4\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll"]),
                   ("imageformats",glob.glob("D:\python3.4\Lib\site-packages\PyQt5\plugins\imageformats\*.dll")),       #解决了不能正常显示gif 的问题
                   ],
      zipfile = None,
       
    options = {'py2exe': py2exe_options},
     
      )

# from distutils.core import setup
# import py2exe
# import sys

# py2exe_options = {
#     "includes": ["sip"],
#     "dll_excludes": ["MSVCP90.dll",],
#     "compressed": 1,
#     "optimize": 2,
#     "ascii": 0,
#     "bundle_files": 1,
#     }

# setup(
#   name = '第一个PyQt5程序',
#   version = '1.0',
#   windows = ['foxmail.py'],
#   zipfile = None,
#   options = {'py2exe': py2exe_options}
#   ) 

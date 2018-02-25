import sys, os
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

__version__ = "0.0.1"

include_files = ['ed.ico',
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                ]
includes = ["os","tkinter","json", "time","threading","math"]
excludes = []
packages = ["os","tkinter","json", "time","threading","math"]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = "ED-Compass",
    description='ED-Compass',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'includes': includes,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("ed_compass.py",base=base)]
)
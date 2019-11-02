import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('brain_check.py', base=base)
]

setup(name='brain_check',
      version='0.1',
      description='Just testing the app',
      options=options,
      executables=executables
      )

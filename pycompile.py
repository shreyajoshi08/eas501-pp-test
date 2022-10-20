#!/bin/python3.7
if __name__ == '__main__':
  import py_compile
  import sys
  import os

  for files in os.listdir():
    if files.endswith('test.py'):
      newFile = files + "c"
      py_compile.compile(files, newFile)

    if files.endswith('unit.py'):
      newFile = files + "c"
      py_compile.compile(files, newFile)


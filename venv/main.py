import ctypes
from ctypes import *
import time
mydll=windll.LoadLibrary("HelloWorld.dll")

print(mydll.PrintName())
time.sleep(10)
print(mydll.AddNumber(1,2))
time.sleep(2)
print(mydll.AddNumber(8,5))
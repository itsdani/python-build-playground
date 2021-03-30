import platform
import numpy as np
from lib_a import lib_a
from bin_a import bin_a

def python_version():
  b = np.arange(15).reshape(3, 5)
  print(bin_a.something_else())
  return lib_a.python_version() * b
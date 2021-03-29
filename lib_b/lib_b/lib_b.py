import platform
import numpy as np
from lib_a import lib_a

def python_version():
  b = np.arange(15).reshape(3, 5)
  return lib_a.python_version() * b
"""python interface to gmsh via Homebrew

This is a simple setup.py script to work with homebrew's install of gmsh.
"""
import os
import subprocess
from setuptools import setup

process = subprocess.run(['brew', '--prefix', '--installed', 'gmsh'],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
brewbasepath = process.stdout.strip()

if process.returncode != 0:
    raise ImportError('Cannot find gmsh in homebrew...\n'
                      '-> Try `homebrew install gmsh` or check your path')

brewlibpath = os.path.join(brewbasepath,'lib')

try:
    sys.path.append(brewlibpath)
    import gmsh as _gmsh
except:
    raise ImportError(f'Cannot find gmsh.py at {brewlibpath}')

version = _gmsh.__version__

setup(
      name='gmsh',
      description='gmsh (via homebrew)',
      longdescription='gmsh.py directly from homebrew',
      version=version,
      package_dir={'': brewlibpath},
      py_modules=['gmsh'],
     )

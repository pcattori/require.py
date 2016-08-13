from __future__ import unicode_literals
import imp
import inspect
import os

# normally python module names cannot contain symbols like '@'
# require.py takes advantage of this to namespace its modules
PREFIX = '@require-'

def require(relative_path):
  '''Returns the module object for the module at the specified relative path.
  Path is relative to calling script's path.
  '''
  # get absolute path by rooting relative path with calling script directory
  caller_relative_filepath = inspect.stack()[1][1]
  caller_root = os.path.dirname(os.path.abspath(caller_relative_filepath))
  absolute_path = os.path.abspath(os.path.join(caller_root, relative_path))

  # compute directory path and filename without extension
  dirpath, filename = os.path.split(absolute_path)
  filename_noext, _ = os.path.splitext(filename)

  # prefixed to avoid module namespace conflicts
  module_name = PREFIX + filename_noext

  spec = imp.find_module(filename_noext, [dirpath])
  return imp.load_module(module_name, *spec)

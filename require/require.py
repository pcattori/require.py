from __future__ import absolute_import
import inspect
import os
import six

# TODO load more than 1x?
def load_module_at(absolute_path):
    '''Loads Python module at specified absolute path. If path points to a
    package, this will load the `__init__.py` (if it exists) for that package.

    :param str absolute_path: Absolute path to the desired Python module.
    :return: Imported Python module
    :rtype: types.ModuleType

    Usage::
      >>> import require
      >>> require.load_module_at('/absolute/path/to/module')
      Module
    '''
    import importlib.util
    if os.path.isdir(absolute_path):
        absolute_path = os.path.join(absolute_path, '__init__.py')

    if not os.path.exists(absolute_path):
        raise ImportError('No module at {}'.format(absolute_path))
    spec = importlib.util.spec_from_file_location(absolute_path, absolute_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def load_py2_module_at(absolute_path):
    '''Loads Python 2 module at specified absolute path. If path points to a
    package, this will load the `__init__.py` (if it exists) for that package.

    :param str absolute_path: Absolute path to the desired Python module.
    :return: Imported Python module
    :rtype: types.ModuleType

    Usage::
      >>> import require
      >>> require.load_module_at('/absolute/path/to/module')
      Module
    '''
    import imp
    if os.path.isdir(absolute_path):
        absolute_path = os.path.join(absolute_path, '__init__.py')

    if not os.path.exists(absolute_path):
        raise ImportError('No module at {}'.format(absolute_path))
    # compute directory path and filename without extension
    dirpath, filename = os.path.split(absolute_path)
    filename_noext, _ = os.path.splitext(filename)

    spec = imp.find_module(filename_noext, [dirpath])
    return imp.load_module(absolute_path, *spec)

def resolve_path(path, upstack=0):
    '''Resolve a path to an absolute path by taking it to be relative to the source
    code of the caller's stackframe shifted up by `upstack` frames.

    :param str path: Filesystem path
    :param int upstack: Number of stackframes upwards from caller's stackframe
    to act as relative point.

    #: TODO Usage example is not great on REPL...

    Usage::
      >>> import require # at /home/require
      >>> require.resolve_path('file.txt')
      '/home/require/file.txt'
    '''
    if os.path.isabs(path):
        return path
    # get absolute path by rooting path with calling script directory
    # TODO guard rails for upstack?
    caller_relative_filepath = inspect.stack()[upstack + 1][1]
    caller_root = os.path.dirname(os.path.abspath(caller_relative_filepath))
    return os.path.abspath(os.path.join(caller_root, path))

def require(path):
    '''Imports Python module at specified path (relative to calling script).

    :param str path: Relative path to the desired Python module. Should be
    relative to the path of the calling script.
    :return: Loaded module
    :rtype: types.ModuleType

    Usage::
      >>> from require import require3 # at /home/user
      >>> foo = require3('./foo.py') # imports /home/user/foo.py
      >>> foo
      Module
      >>> bar = require3('../arbitrary/path/bar.py') # imports /home/arbitrary/path/bar.py
      >>> bar
      Module
      >>> baz = require3('/absolute/path/bar.py') # imports /absolute/path/baz.py
      >>> baz
      Module
    '''
    absolute_path = resolve_path(path, upstack=1)
    if six.PY2:
        return load_py2_module_at(absolute_path)
    return load_module_at(absolute_path)


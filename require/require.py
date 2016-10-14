import importlib.util
import inspect
import os

# TODO load more than 1x?
def load_module_at(absolute_path):
    '''Loads Python module at specified absolute path.

    :param str absolute_path: Absolute path to the desired Python module.
    :return: Imported Python module
    :rtype: Module

    Usage::
      >>> import require
      >>> require.load_module_at('/absolute/path/to/module')
      Module
    '''
    if os.path.isdir(absolute_path):
        absolute_path = os.path.join(absolute_path, '__init__.py')

    if not os.path.exists(absolute_path):
        raise ImportError('No module at {}'.format(absolute_path))
    spec = importlib.util.spec_from_file_location(absolute_path, absolute_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

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
    caller_relative_filepath = inspect.stack()[upstack + 1][1]
    caller_root = os.path.dirname(os.path.abspath(caller_relative_filepath))
    return os.path.abspath(os.path.join(caller_root, path))

# TODO python2/3 compatible?
def require3(path):
    '''
    :param str path: Relative path to the desired Python module. Should be
    relative to the path of the calling script.

    Usage::
      >>> import require # at /arbitrary/path
      >>> foo = require.require3('./foo.py') # imports /arbitrary/path/foo.py
      >>> foo
      Module
    '''
    absolute_path = resolve_path(path, upstack=1)
    return load_module_at(absolute_path)


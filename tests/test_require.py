from require import require
import os
import subprocess
import tempfile
import unittest
import sh

lib_code = '''# lib.py
def hello():
    return 'world'
'''

app_code_template = '''
from require import require
lib = require.require3('{}')
print(lib.hello())
'''

garbage = '''lfasjdlfkjasoifdphoq'''

def app_setup(path, lib_relative):
    place_at_path(app_code_template.format(lib_relative), path)

def lib_setup(path):
    place_at_path(lib_code, path)

def place_at_path(contents, path):
  sh.mkdir('-p', os.path.dirname(path))
  with open(path, 'w') as f:
    f.write(contents)

class RequireTest(unittest.TestCase):

  def test_sibling(self):
    with tempfile.TemporaryDirectory() as tmp:

      app = os.path.join(tmp, 'app.py')
      app_setup(app, './lib.py')

      lib = os.path.join(tmp, 'lib.py')
      lib_setup(lib)

      stdout = subprocess.check_output(['python', app])
      self.assertEqual(stdout, b'world\n')

  def test_descendant(self):
    with tempfile.TemporaryDirectory() as tmp:
      app = os.path.join(tmp, 'app.py')
      app_setup(app, './directory/lib.py')

      lib = os.path.join(tmp, 'directory', 'lib.py')
      lib_setup(lib)

      stdout = subprocess.check_output(['python', app])
      self.assertEqual(stdout, b'world\n')

  def test_ancestor(self):
    with tempfile.TemporaryDirectory() as tmp:
      app = os.path.join(tmp, 'directory', 'app.py')
      app_setup(app, '../lib.py')
      lib = os.path.join(tmp, 'lib.py')
      lib_setup(lib)

      stdout = subprocess.check_output(['python', app])
      self.assertEqual(stdout, b'world\n')

  def test_arbitrary(self):
    with tempfile.TemporaryDirectory() as tmp:
      app = os.path.join(tmp, 'directory', 'app.py')
      app_setup(app, '../folder/lib.py')
      lib = os.path.join(tmp, 'folder', 'lib.py')
      lib_setup(lib)

      stdout = subprocess.check_output(['python', app])
      self.assertEqual(stdout, b'world\n')

  def test_absolute(self):
    with tempfile.TemporaryDirectory() as tmp:
      app = os.path.join(tmp, 'app.py')
      lib = os.path.join(tmp, 'lib.py')
      app_setup(app, lib)
      lib_setup(lib)

      stdout = subprocess.check_output(['python', app])
      self.assertEqual(stdout, b'world\n')


  # package with __init__


  # ImportError for non-sense
    # no file found
    # not python file

  # TODO caching... maybe we should handle that?

if __name__ == '__main__':
  unittest.main()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
]

source_suffix = '.rst'

master_doc = 'index'

project = 'require.py'
copyright = '2016, Pedro Cattori'
author = 'Pedro Cattori'

version = '2.0.0'
release = '2.0.0'

language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'alabaster'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = '_static/jellyfish.png'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'require.pydoc'


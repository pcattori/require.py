[![PyPI version](https://badge.fury.io/py/require.py.svg)](https://badge.fury.io/py/require.py)
[![Build Status](https://travis-ci.org/pcattori/require.py.svg?branch=master)](https://travis-ci.org/pcattori/require.py)

# require.py

Inspired by [require.js](http://requirejs.org/)

## Install

```bash
$ pip install require.py
```

## Usage

### python 3.5+

```python
from require import require
mod = require('relative/path/to/module.py')

# alternatively, use absolute path
mod = require('/absolute/path/to/module.py')
```

### python2.7

Use `require2` instead:

```python
from require import require
mod = require2('relative/path/to/module.py')

# alternatively, use absolute path
mod = require2('/absolute/path/to/module.py')
```

## Example

directory structure:
- test/
  - bar-directory/
    - bar.py
  - foo-directory/
    - foo.py

```python
# bar-directory/bar.py
CONST = 'string constant'

def hello():
  return 'world'
```

```python
# foo-directory/foo.py
from require import require
bar = require('../bar-directory/bar.py')

print bar.CONST
print bar.hello()
print dir(bar)
```

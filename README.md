# require.py

Inspired by [require.js](http://requirejs.org/)

## Install

```bash
$ pip install require.py
```

## Usage

```python
import require
mod = require.py('relative/path/to/module')
```

## Example

directory structure:
- test/
  - bar.py
  - foo/
    - foo.py

```python
# bar.py
CONST = 'string constant'

def hello():
  return world
```

```python
# foo
import require
bar = require.py('../bar') # '.py' extension is optional

print bar.CONST
print bar.hello()
print dir(bar)
```

# require.py

Inspired by [Node.js](http://node.org/) `require`

## Install

```bash
$ pip install require.py
```

## Usage

```python
import require
mod = require.py('relative/path/to/module')

# alternatively, use explicit './' prefix
mod = require.py('./relative/path/to/module')
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
  return world
```

```python
# foo-directory/foo
import require
bar = require.py('../bar-directory/bar') # '.py' extension is optional

print bar.CONST
print bar.hello()
print dir(bar)
```

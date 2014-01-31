PyPasswordr
===========

A python variant of my (https://github.com/aapis/passwordr)[Passwordr] project.

## Usage

```python
_arg = {
	"base": "whatever", #uses this as a salt, optional
	"length": 32,
}

python passwordr.py _arg["base"] _arg["length"]
```
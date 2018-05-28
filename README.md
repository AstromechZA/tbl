# `tbl` - Readme

[![Build Status](https://travis-ci.org/AstromechZA/tbl.svg?branch=master)](https://travis-ci.org/AstromechZA/tbl)

Simple table printing for Python CLI tools.

**NOTE:** until this notice is removed from this file - this project should be considered a work in progress and should not be relied on!

## How to install

```
$ python setup.py install
```

## Development

```
$ virtualenv --no-site-packages venv && source venv/bin/activate
$ python setup.py develop
```

And then run the tests with:

```
$ python setup.py test
```

If you need test dependencies for writing new tests, you can install them with:

```
$ pip install .[test]
```

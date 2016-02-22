# Pycaesar [![Build Status](https://snap-ci.com/nicolastrres/pycaesar/branch/master/build_image)](https://snap-ci.com/nicolastrres/pycaesar/branch/master)  [![Requirements Status](https://requires.io/github/nicolastrres/pycaesar/requirements.svg?branch=master)](https://requires.io/github/nicolastrres/pycaesar/requirements/?branch=master) [![PyPi version](https://img.shields.io/pypi/v/pycaesar.svg)](https://pypi.python.org/pypi/pycaesar)
### Caesar cipher in python 

Simple caesar cipher in python.


IMPORTANT: This is not secure and should not be used for a purpose other than have fun.


#### How to install

Just run `pip install pycaesar` and have fun :)

#### How to use pycaesar

You can encrypt/decrypt from the command line:
```ssh
usage: Pycaesar [-h] {encrypt,decrypt} key message

A simple caesar cipher in python. 

optional arguments:
  -h, --help         show this help message and exit

Encryption options:
  {encrypt,decrypt}  Encrypt or decrypt?
  key                Key is a numeric value to encrypt the message
  message            Message to be encrypted

And that is the way you encrypt/decrypt data using the caesar cipher algorithm
```
Examples:
```
pycaesar encrypt 2 'agustin nicolas'
pycaesar decrypt 2 'ciwuvkp pkeqncu'
```


#### Contributing

1. Fork the repository https://github.com/nicolastrres/pycaesar/fork
2. Create a new virtual environment `pyvenv ~/.virtualenvs/pycaesar && source ~/.virtualenvs/pycaesar/bin/activate`
3. Install the requirements `pip install -r requirements.txt`
4. Write your tests on tests/
5. Run `py.test --cov=caesar tests/test.py` to see the test coverage
6. Run the tests `py.test tests/test.py`
7. Run `flake8 caesar tests`
8. Push your changes and make a pull request.


##License 
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

The MIT License (MIT)

Copyright (c) 2016 Nicolas Agustin Torres, https://github.com/nicolastrres

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

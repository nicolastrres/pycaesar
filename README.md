# Pycaesar [![Build Status](https://snap-ci.com/nicolastrres/pycaesar/branch/master/build_image)](https://snap-ci.com/nicolastrres/pycaesar/branch/master)
### Caesar cipher in python 

Simple caesar cipher in python.


IMPORTANT: This is not secure and should not be used for a purpose other than have fun.


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
python3.4 caesar/__main__.py encrypt 2 'agustin nicolas'
python3.4 caesar/__main__.py decrypt 2 'ciwuvkp pkeqncu'
```


#### Contributing

1. Fork the repository https://github.com/nicolastrres/pycaesar/fork
2. Create a new virtual environment `pyvenv ~/.virtualenvs/pycaesar && source ~/.virtualenvs/pycaesar/bin/activate`
3. Install the requirements `pip install -r requirements.txt`
4. Write your tests on tests/
5. Run the tests `py.test tests/test.py`
6. Run `flake8 caesar tests`
7. Push your changes and make a pull request.

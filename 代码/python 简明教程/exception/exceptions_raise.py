# encoding=UTF-8

class ShortInputException(Exception):
    '''用户自定义的异常类'''
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter sth --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('EOF')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
    '{0} long, expected at least {1}')
    .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

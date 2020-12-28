from parse import parse, compile
from hooks import decimal

string = 'I'
string1 = 'C..18'
string2 = 'D10.5'

def hookParser(string):
    fixed = ['I','F']
    patterns = ['C{n:d}','C..{n:d}','I..{n:d}','D{w:d}.{d:d}']
    if string in fixed:
        return {string:0}
    else:
        for pattern in patterns:
            regex = compile(pattern)
            result = regex.parse(string)
            if result != None:
                return result.named

def hookMaker(format):
    keys = [key for key in format.keys()]
    key = keys[-1]
    if key == 'I':
        hook = 'decimal0'
    elif key == 'd':
        hook = f'decimal{format["d"]}'
    else:
        hook = ''
    return hook


result = hookParser(string2)
hook = hookMaker(result)
print(hook)
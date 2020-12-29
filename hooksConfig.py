from parse import parse, compile
from hooks import decimal
import pandas as pd
import numpy as np

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
                print('result:',result)
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

def readReportRule(filename):
    
    all = pd.read_excel(filename,sheet_name=None)
    sheetNames = all.keys()
    for sheetName in sheetNames:
        print(sheetName)
        df = pd.read_excel(filename,sheet_name=sheetName)
        df.drop(df[np.isnan(df['序号'])].index, inplace=True)
        df['hook'] = df['长度'].apply(lambda x: hookMaker(hookParser(x)))
    return df


df = readReportRule('报表规范.xls')
print(df)
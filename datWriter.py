import os
import pandas as pd
from configHandler import configReader
from hooks import *


def datWriter(filename, reportConfig, path=''):
    df = pd.read_excel(filename, header=0, sheet_name=0)
    columnNames = list(df)
    for key, value in reportConfig.items():
        print(value)
        # df[key] = df[key].map(lambda x: f'{x:.{value}f}')
        columnName = columnNames[key-1]
        df[columnName] = df[columnName].map(lambda x: value(x))
    content = df.to_csv(None, header=False, index=False,
                        sep='|', encoding='utf-8')
    # to_csv会自动多空一行，手动去除后两行写入文件
    datFilename = os.path.join(path, filename.replace('xlsx', 'dat'))
    with open(datFilename, 'w', newline='', encoding='utf-8') as f:
        f.write(content[:-2])


if __name__ == '__main__':
    rules = configReader('rule.dict')
    filename = '91341700573031656T_CLGRDK_20201130.xlsx'
    datWriter(filename, rules)

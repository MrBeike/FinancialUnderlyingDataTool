import pandas as pd


def datWriter(filename, config):
    orgCode, reportCode, date = filename.split('_')
    df = pd.read_excel(filename, header=0, sheet_name=0)
    columnNames = list(df)
    reportConfig = config[reportCode]
    for key, value in reportConfig.items():
        # FIXME 字符串是否可以用
        # df[key] = df[key].map(lambda x: f'{x:.{value}f}')
        columnName = columnNames[key-1]
        df[columnName] = df[columnName].map(lambda x: value)
    content = df.to_csv(None, header=False, index=False,
                        sep='|', encoding='utf-8')
    # to_csv会自动多空一行，手动去除后两行写入文件
    with open(filename.replace('xlsx', 'dat'), 'w', newline='', encoding='utf-8') as f:
        f.write(content[:-2])


filename = '91341700573031656T_CLGRDK_20201130.xlsx'
datWriter(filename, rules)

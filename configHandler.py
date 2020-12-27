import pickle
from hooks import decimal0, decimal2, decimal5, idMask, dateParser

# 设置dict规则适配数据列特殊处理函数
rules = {
    'CLTYJD': {11: decimal2, 12: decimal2,  14: decimal5,  16: decimal5},
    'TYJDFS': {13: decimal2, 14: decimal2,  16: decimal5,  18: decimal5},
    'CLDWDK': {19: decimal2, 20: decimal2,  22: decimal5,  24: decimal5},
    'DWDKFS': {19: decimal2, 20: decimal2,  22: decimal5,  24: decimal5},
    # 'CLGRDK': {14: decimal2, 15: decimal2,  17: decimal5,  19: decimal5},
    'CLGRDK': {10: dateParser, 11: dateParser, 12: dateParser, 14: decimal2, 15: decimal2,  17: decimal5,  19: decimal5, 21: dateParser},
    'GRDKFS': {14: decimal2, 15: decimal2,  17: decimal5,  19: decimal5},
    'CLZXDK': {},
    'DBHTXX': {10: decimal2, 11: decimal2,  12: decimal2},
    'DBWXX': {11: decimal2, 13: decimal2,  14: decimal2},
    'CLWTDK': {18: decimal2, 19: decimal2,  21: decimal5,  22: decimal2},
    'WTDKFS': {18: decimal2, 19: decimal2,  21: decimal5,  22: decimal2},
    'JRJGFZ': {},
    'TYKHXX': {15: decimal0, 16: decimal0},
    'FTYKHX': {8: decimal2, 9: decimal2,  10: decimal2,  11: decimal2,  12: decimal0,  23: decimal2,  24: decimal2,  28: decimal0,  29: decimal0},
    'GRKHXX': {10: decimal2, 11: decimal2,  14: decimal2,  15: decimal2,  19: decimal0,  20: decimal0},
    'CLTYCK': {11: decimal2, 12: decimal2,  13: decimal5},
    'TYCKFS': {11: decimal2, 12: decimal2,  15: decimal5},
    'FTYDWC': {13: decimal2, 14: decimal2,  15: decimal5},
    'DWCKFS': {14: decimal2, 15: decimal2,  16: decimal5},
    'CLGRCK': {12: decimal2, 13: decimal2,  14: decimal5},
    'GRCKFS': {13: decimal2, 14: decimal2,  15: decimal5},
    'CLZQTZ': {8: decimal2, 9: decimal2,  13: decimal5},
    'ZQTZFS': {11: decimal5, 20: decimal2,  21: decimal2},
    'CLZQFX': {6: decimal0, 8: decimal2,  9: decimal2,  10: decimal2,  11: decimal2,  16: decimal5},
    'ZQFXFS': {6: decimal0, 8: decimal2,  9: decimal2,  10: decimal2,  11: decimal2,  16: decimal5},
    'CLGQTZ': {9: decimal2, 10: decimal2},
    'GQTZFS': {10: decimal2, 11: decimal2},
    'SPVTZX': {12: decimal2, 13: decimal2},
    'SPVFSX': {13: decimal2, 14: decimal2},
    'WQYBJY': {7: decimal2},
}


def configWriter(obj, filename):
    fileHandler = open(filename, 'wb')
    pickle.dump(obj, fileHandler)
    fileHandler.close()
    return


def configReader(filename):
    fileHandler = open(filename, 'rb')
    rule = pickle.load(fileHandler)
    fileHandler.close()
    return rule


if __name__ == '__main__':
    configWriter(rules, 'rule.dict')

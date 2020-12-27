#:toolbox: FUDT--FinancialUnderlyingDataTool

## 简介
金融基础数据采集报表辅助工具，依据《金融基础数据采集规范》对金融机构的金融基础数据报表进行上报前处理，包括身份信息脱敏、特定小数位处理等。

## 流程
读取Excel文件 >> 根据规则处理数据（*rule.dict* ,*confighanlder.py*）>> 保存处理好的数据为dat文件(*datWriter.py*) >> 根据dat文件生成对应的log文件（*logWriter.py*） >> 将生成好的文件存入压缩包（*zipFile.py*）

## 进展
[]API
- []Excel报表读取
- []规则处理函数
- []保存dat文件
- [X]生成log文件
- []生成压缩包
[]GUI
- []UI设计
- []slot函数定义
 
# :toolbox: FUDT--FinancialUnderlyingDataTool

## 简介
金融基础数据采集报表辅助工具，依据《金融基础数据采集规范》对金融机构的金融基础数据报表进行上报前处理，包括身份信息脱敏、特定小数位处理等。

## 流程
读取Excel文件 >> 根据规则处理数据（*rule.dict* ,*confighanlder.py*）>> 保存处理好的数据为dat文件(*datWriter.py*) >> 根据dat文件生成对应的log文件（*logWriter.py*） >> 将生成好的文件存入压缩包（*zipFile.py*）

## 进展
### API
- [X] Excel报表读取
- [ ] 规则处理函数
  - [X] 规则文件写入保存
  - [ ] 规则函数编写
  - [ ] 规则列表完善 
- [X] 保存dat文件
- [x] 生成log文件
- [X] 生成压缩包
- [ ] 清理工作空间或设置子空间？
### GUI
- [ ] UI设计
- [ ] slot函数定义

## 待解决/计划
  + 加入错误提示功能（错误日志？）
  + 已知报表中日期格式数据填错时（1900-01-01），获取的数据为datetime.time类型（正常为datetime.date），无法进行datetime.strftime()处理.
 
## 赞赏
如果你觉得这个工具很赞,可以赞赏作者给予鼓励。（下次一定也OK:joy:）

<img src="donate.png">

## 红楼一梦
            春梦随云散
            飞花逐水流
            寄言众儿女
            何必觅闲愁

Hope you get your own happines,sincerely.
Cause I know it's hard, but it worths.
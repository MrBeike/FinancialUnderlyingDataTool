from zipFile import zipFile
from logWriter import logWriter
from configHandler import configReader
from datWriter import datWriter
import os


class FUDT:
    def __init__(self):
        self.configFilename = 'rule.dict'

    def getFileInfo(self):
        fileUrl = input('请输入EXCEl文件完整路径：')
        if fileUrl:
            filePath, filename = os.path.split(fileUrl)
            pureFilename, extension = os.path.splitext(filename)
            orgCode, reportCode, date = filename.split('_')
            self.filePath = filePath
            self.filename = filename
            self.pureFilename = pureFilename
            self.reportCode = reportCode
            self.date = date
        return

    def configHandler(self):
        config = configReader(self.configFilename)
        self.reportConfig = config[self.reportCode]
        return

    def datFileGenerater(self):
        datWriter(self.filename, self.reportConfig, path=self.filePath)

    def logFileGenerater(self):
        datFilename = f'{self.pureFilename}.dat'
        logWriter(datFilename, path=self.filePath)

    def zipFileGenerater(self):
        zipFile(self.pureFilename, path=self.filePath)

    # TODO 新建工作子目录 Or 当前目录处理并清理
    def workDirClean(self):
        pass


if __name__ == '__main__':
    fudt = FUDT()
    fudt.getFileInfo()
    fudt.configHandler()
    fudt.datFileGenerater()
    fudt.logFileGenerater()
    fudt.zipFileGenerater()
    fudt.workDirClean()
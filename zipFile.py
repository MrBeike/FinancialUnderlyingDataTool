import os


def workDirClean():
    fileList = os.listdir(workDir)
    for eachfile in fileList:
        try:
            suff = eachfile.split('.')[1]
            if suff in ['dat', 'log']:
                os.remove(eachfile)
        except IndexError:
            pass


def getfileNames():
    '''
    获取工作文件夹下所有的xlsx格式文件

    '''
    fileList = os.listdir(workDir)
    excelFiles = []
    for eachfile in fileList:
        try:
            suff = eachfile.split('.')[1]
            if suff == 'xlsx':
                excelFiles.append(eachfile)
        except IndexError:
            pass
    return excelFiles


def zipFiles(fileName):
    fileName_pre = fileName.split('.')[0]
    zipFile = zipfile.ZipFile(os.path.join(
        workDir, fileName_pre) + '.zip', 'w', zipfile.ZIP_DEFLATED)
    f_txt = fileName_pre + '.dat'
    f_log = fileName_pre + '.log'
    try:
        zipFile.write(os.path.join(workDir, f_txt), arcname=f_txt)
        zipFile.write(os.path.join(workDir, f_log), arcname=f_log)
        zipFile.close()
        print(f'{fileName}报表压缩包搞定啦！')
    except:
        print(f'{fileName}报表dat文件或log文件丢失，请尝试重新运行本程序')

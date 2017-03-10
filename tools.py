#coding: utf-8
import md5
import ftplib
from shutil import *
import os.path
import time
from os.path import *
import sys
import subprocess
rarexe_path = r'C:\Program Files\WinRAR\WinRAR.exe'

def chTime(timeValue):
    return time.strftime("%m",timeValue)+"月"+time.strftime("%d",timeValue)+"日"

class deploy:

    def FTP(self):
        return self.__ftp

    def __init__(self):
        self.__ftp = ftplib.FTP()
        self.__ftp.timeout = 50
        self.__ftp.encoding = "GBK"

    def disconnect(self):
        self.__ftp.quit()
        print("ftp断开连接")

    def connect(self):
        self.__ftp.connect("192.168.60.207")
        self.__ftp.login("szk", "szk_202")
        print(self.__ftp.welcome)

    def mkd(self,rmPath):
        parentPath,subPath = os.path.split(rmPath)
        fs = self.__ftp.nlst(parentPath)
        if(subPath=="")or(fs == [])or(parentPath + "/" + subPath not in fs):
            self.mkd(parentPath)
        if(not subPath=="")and(parentPath + "/" + subPath not in fs):
            self.__ftp.mkd(parentPath + "/" + subPath)

    def zipToFile(self, Files, zipFile,param = ""):
        os.chdir("C:\Program Files\WinRAR")
        if(isinstance(Files, str)):
            add_command = "winrar a -u -ep1 -ibck -ap\"{0}\" {1} {2} ".format(param, zipFile, Files)
            print(add_command)
            subprocess.call([rarexe_path, 'a', '-u','-ep1','-ibck','-ap%s' %(param), zipFile, Files])
            #os.system(add_command)
        else:
            filesStr = ""
            for f in Files:
                filesStr = "\"" + f + "\" " + filesStr
            add_command = "winrar a -u -ep1 -ibck {0} {1} ".format(zipFile, filesStr)
            os.system(add_command)

    def updateZip(self, srcFile, desFile,zipFile,compare=1):
        if(compare==0)or(md5.md5_file(srcFile) != md5.md5_file(desFile)):
            if srcFile != desFile:
                copyfile(srcFile, desFile)
            print("copy " + srcFile)
            self.zipToFile(desFile, zipFile)
            print("zip ok")
            return 1
        else:
            print(desFile + " not need update")
            return 0

    def checkUpdate(self,files, src, des):
        updateFiles = []
        for file in files :
            if(not isfile(join(des,file))or(md5.md5_file(join(src, file)) != md5.md5_file(join(des,file)))):
                copyfile(join(src, file), join(des,file))
                updateFiles.append(join(des,file))
        return updateFiles

    def updateDirToFtp(self,localFile,rmtPath):
        for parent,dirnames,filenames in os.walk(localFile):
            for dirname in  dirnames:
                self.updateDirToFtp(os.path.join(localFile, dirname),rmtPath + dirname + "/")
            for filename in filenames:
                if os.path.isfile(os.path.join(localFile, filename)):
                    self.updateFileToFtp(os.path.join(localFile,filename),rmtPath)

    def updateFileToFtp(self,localFile,rmtPath):
        print("创建目录 " + rmtPath)
        self.mkd(rmtPath)
        rmtFile = rmtPath + os.path.basename(localFile)
        print("上传文件 " + localFile + " 到 "+rmtPath)
        f=open(localFile, "rb")
        mt=time.gmtime(os.path.getmtime(localFile))
        mts = time.strftime("%Y%m%d%H%M%S", mt)
        self.__ftp.storbinary("STOR " + rmtFile, f)
        print("上传完成")
        self.__ftp.sendcmd("MDTM " + mts + " " + rmtFile)


    def updateToFtp(self, localPath, rmtPaths):
        for rmtPath in rmtPaths:
            if os.path.isdir(localPath):
                self.updateDirToFtp(localPath, rmtPath)
            else:
                self.updateFileToFtp(localPath, rmtPath)
        print("update " + localPath + " finished")

    def updateRmtPaths(self,rmtPaths,subPath):
        desPaths = []
        for rmtPath in rmtPaths:
            desPaths.append(os.path.join(rmtPath,subPath))
        return desPaths

    def downloadFromFtp(self,localPath, rmtPath):
        self.mkd(rmtPath)
        ot = open(localPath, "wb")
        print("RETR %s " % rmtPath)
        self.__ftp.retrbinary("RETR %s" % rmtPath, ot.write)

    def downloadFolderFromFtp(self,localPath,rmtPath):
        l = self.__ftp.nlst(rmtPath)
        if(not os.path.exists(localPath)):
            os.makedirs(localPath)
        for f in l:
            p = []
            self.__ftp.dir(rmtPath, p.append)
            p1 = p.pop(0)
            subDir = basename(f)
            if(p1.startswith('d')):
                self.downloadFolderFromFtp(join(localPath, subDir), f)
            else:
                self.downloadFromFtp(join(localPath, subDir), f)

    def ftpfileExist(self,rmtPath):
        parentPath,subPath = os.path.split(rmtPath)
        fs = self.__ftp.nlst(parentPath)
        return parentPath+"/" + subPath in fs

    def ftpListFiles(self,rmtPaht):
        return self.__ftp.nlst(rmtPaht)

class localSign():
    __Ext = [".dll",".exe"]

    def __cur_file_dir(sef):
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

    def signFile(self,file):
        path,ext = os.path.splitext(file)
        if(ext in self.__Ext):
            cp = self.__cur_file_dir()
            os.chdir(cp)
            cmd = "signtool.exe sign /f servyou.pfx /p password /t http://timestamp.verisign.com/scripts/timstamp.dll \"" + file + "\""
            print(cmd)
            print(os.system(cmd))

class sign():

    def __init__(self):
        self.__ftp = ftplib.FTP()
        self.__ftp.timeout = 2000
        self.__ftp.encoding = "GBK"
        self.__ftp.connect("192.168.102.201")
        self.__ftp.login("guoxl", "guoxl123")
        self.__fileList = []
        print(self.__ftp.welcome)

    def signFile(self,file):
        print("update to sign")
        self.__fileList.append(file)
        self.__ftp.storbinary("STOR input/" + os.path.basename(file),open(file,"rb"))
        print("update to sign end")

    def waitForSign(self):
        waitT = 0;
        while len(self.__fileList) > 0 :
            list = self.__ftp.nlst("output")
            waitT = waitT + 1
            print(waitT)
            check = 0
            for l in self.__fileList:
                if list.count(os.path.basename(l)) >0:
                    print(l + " sign success")
                    self.__fileList.remove(l)
                    self.__ftp.retrbinary("RETR output/"+os.path.basename(l), open(l,"wb").write)
                    self.__ftp.delete("output/"+os.path.basename(l))
                    check =1
                    break
            if check==0:
                time.sleep(5)


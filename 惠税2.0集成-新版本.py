#coding: utf-8
from tools import *
from shutil import *
from os import *
import subprocess
TortoiseProcPath = r'C:\Program Files\TortoiseSVN\bin\TortoiseProc.exe'
rarexe_path = r'C:\Program Files\WinRAR\WinRAR.exe'

import shutil
try:
    shutil.rmtree(r'D:\项目\惠税2.0集成\三方成果\应用工具')#删除
except Exception as e:
    pass


try:
    d = deploy()
    d.connect()

    nh = int(time.strftime("%H"))
    if(nh>=8)and(nh<11):
        depTimes = "一"
    elif nh < 17:
        depTimes = "二"
    else:
        depTimes = "三"
    da = chTime(time.gmtime())
    ftpRoot = "//河北惠税2.0总集成//项目集成//"+da+"//第"+depTimes+"次集成-已签名"

    d.downloadFolderFromFtp("D:\项目\惠税2.0集成\三方成果","/河北惠税2.0总集成/项目集成/三方成果/")

    os.chdir("D:\项目\惠税2.0集成\Build")
    subprocess.call([TortoiseProcPath, '/command:update', '/closeonend:1', '/path:D:\项目\惠税2.0集成\Build\installsource\YQHS'])
    system("D:\项目\惠税2.0集成\\Build\\build_yqhs_jcss.cmd")
    
    subprocess.call([TortoiseProcPath, '/command:update', '/closeonend:1', '/path:D:\项目\惠税2.0集成\Build\swy_installsource'])
    system("D:\项目\惠税2.0集成\\Build\\build_swy.cmd")

    system("D:\项目\惠税2.0集成\\Build\\build_cef.cmd")

    # # 上传
    d.updateToFtp("D:\项目\惠税2.0集成\Build\installer\SWYInst_09390100010000(国税税无忧工具箱).exe", [ftpRoot + "//应用工具//"])
    d.updateToFtp("D:\项目\惠税2.0集成\Build\installer\yqhsjcssInst_092801HB010000.exe", [ftpRoot + "//应用工具//"])
    d.updateToFtp("D:\项目\惠税2.0集成\Build\installer\DMInst_CEF1650.exe", [ftpRoot + "//应用工具//"])

    zipFile = "D:\项目\惠税2.0集成\三方成果\应用工具\河北公司（单企业版）版本号.exe"
    upFile = "D:\项目\惠税2.0集成\\三方成果\平台\门户\InstallEPPortal(无数据迁移).dat"
    copyfile(upFile,"D:\项目\惠税2.0集成\\三方成果\平台\门户\InstallEPPortal.dat")

    subprocess.call([rarexe_path, 'a', '-u','-ep1','-ibck','-ap%s' %('Files\Packages\\03350100030000_易税门户V3.0'), zipFile, 'D:\项目\惠税2.0集成\\三方成果\平台\门户\InstallEPPortal.dat'])
    d.updateToFtp(upFile, [ftpRoot +  "//平台//门户//"])

    upFile = "D:\项目\惠税2.0集成\\三方成果\平台\通用申报\jdls_DZSB.dat"
    subprocess.call([rarexe_path, 'a', '-u','-ep1','-ibck','-ap%s' %('Files\Packages\\07250100060000_通用申报软件V7.1'), zipFile, upFile])
    d.updateToFtp(upFile, [ftpRoot +  "//平台//通用申报//"])
    d.updateToFtp(zipFile, [ftpRoot + "//应用工具//"])

    upFile = "D:\项目\惠税2.0集成\\三方成果\应用工具"
    loPaths = os.listdir(upFile)
    for loPath in loPaths:
        rmtPath = os.path.basename(loPath)
        if(loPath.count("PWYInstV")>0):
            upFile= join("D:\项目\惠税2.0集成\三方成果\应用工具",loPath)
            break
    d.updateToFtp(upFile, [ftpRoot +  "//应用工具//"])

    

    input("部署完成，可以关闭程序")
except Exception as e:
    input(e)

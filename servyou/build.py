import shutil, os, os.path, zipfile, sys
import subprocess


baseDir = r'D:\servyou\NSGLWMH'
preVersion = 'V1.0.022'
version = 'V1.0.023'
subApp = 'NSGLWMH'
dll_name = 'NSGLwmhMain.dll'
rarexe_path = r'C:\Program Files\WinRAR\WinRAR.exe'

#清除app解压出来的_temp文件
def clear_temp(dir):
	print('clear dir %s temp file' %dir)
	for path,dirnames,filenames in os.walk(dir):
		for filename in filenames:
			if  filename.endswith('.app'):
				#os.remove(os.path.join(path, filename))
				tempFile = os.path.join(path, filename[0:-4]+'_temp.xml') 
				f = os.path.join(path, filename[0:-4]+'.xml')
				if os.path.exists(tempFile):
					os.remove(tempFile)
					print('remove-->'+ tempFile)
				if os.path.exists(f):
					os.remove(f)
					print('remove-->'+ f)


#移动编译好后的dll到未签名


original_dll_dir = r'D:\servyou\EPPortal_GS3.0\AppModules\%s\%s' % (subApp, dll_name)
target_dll_dir = r'%s\%s\0000\upgradeFiles\未签名\AppModules\%s\%s' %(baseDir, version, subApp, dll_name)

#shutil.copy(original_dll_dir, target_dll_dir)

def copyUnsign2Sign():
	signdir = r'%s\%s\0000\upgradeFiles\已签名' %(baseDir, version)
	unsignDir = r'%s\%s\0000\upgradeFiles\未签名' %(baseDir, version)
	# 先删除已签名文件夹
	if os.path.exists(signdir):
		shutil.rmtree(signdir)
	shutil.copytree(unsignDir, signdir)
	print('copy %s to %s' %(unsignDir, signdir))

#签名dll
def sigDll(version):

	unsignDir = r'%s\%s\0000\upgradeFiles\未签名' %(baseDir, version)
	signDir = r'%s\%s\0000\upgradeFiles\已签名' %(baseDir, version)
	dlls = []
	# 找到所有dll文件
	for root, dirs, files in os.walk(unsignDir):
		for f in files:
			if f[-3:].lower() == 'dll' or f[-3:].lower() == 'exe' or f[-3:].lower() == 'bpl':
				dllFile = os.path.join(root, f)
				print('find dll-->' + dllFile)
				dlls.append(dllFile)

	if len(dlls) == 0: return
	# 连接ftp 
	import ftplib
	from ftplib import FTP
	import time
	with FTP('192.168.102.201') as ftp:
		ftp.login('liyg', 'liyg123')

		#上传dll 文件到 /input
		ftp.cwd('/input')
		for dll in dlls:
			f = open(dll, 'rb')
			file_name = os.path.basename(dll)
			try:
				ftp.storbinary('STOR %s' %file_name, f)
			except ftplib.error_perm:
				print('upload file %s failed'% file_name)
			else:
				print('upload file %s success'% file_name)
		
		#从 /output 里取签名好的dll
		ftp.cwd('/output')
		while dlls:
			time.sleep(10)
			for dll_unsign in dlls:
				dll_sign = dll_unsign.replace('未签名', '已签名')
				
				file_name = os.path.basename(dll_sign)
				try:
					if  file_name in ftp.nlst():
						f = open(dll_sign, 'wb').write
						try:
							ftp.retrbinary('RETR %s'%file_name, f)
						except ftplib.error_perm:
							print('download file %s fail'%file_name)
						else:
							print('download file %s success'% file_name)
							ftp.delete(file_name)
							dlls.remove(dll_unsign)
				except ftplib.error_perm:
					print('ftp.nlst() error')

# upgrade文件夹下制作V1.1.012_V1.1.013.zip文件
def makeUpgrade(preVersion, version):
	zipFileName = r'%s_%s.zip' %(preVersion, version)
	root_dir = r'%s\%s\0000\upgradeFiles\已签名' % (baseDir, version)
	zipFilePath = r'%s\%s\0000\upgrade\%s' % (baseDir, version, zipFileName)

	subprocess.call([rarexe_path, 'a', '-ep1', '-r', zipFilePath, '%s\\*' %(root_dir)])
	print('create zipfile %s' %zipFileName)


#installsource文件夹下 制作jdls_NSGLWMH.dat
# 取上一版本的dat，覆盖此次的签名成果
def makeInstallsource(preVersion, version):
	preVersionDatFile = r'%s\%s\0000\installsource\jdls_NSGLWMH.dat' %(baseDir, preVersion)
	tempDir = r'%s\temp' %(baseDir)
	installsourceDir = r'%s\%s\0000\installsource' %(baseDir, version)
	signedDir = r'%s\%s\0000\upgradeFiles\已签名' % (baseDir, version)
	
	subprocess.call([rarexe_path, 'x', preVersionDatFile, tempDir])

	#覆盖此次已签名版本
	# /s 递归复制 /y  覆盖文件
	subprocess.call(['xcopy', signedDir, tempDir, '/s', '/y'])  

	#压缩为.zip包
	zipFileName = 'jdls_NSGLWMH.zip'
	zipFilePath = r'%s\%s' %(installsourceDir, zipFileName)
	#shutil.make_archive(base_name, 'zip', root_dir, '.')
	subprocess.call([rarexe_path, 'a', '-ep1', '-r', zipFilePath, '%s\\*' %(tempDir)])

	# 删除\AppComs \AppModules 文件夹
	shutil.rmtree(os.path.join(tempDir, 'AppComs'))
	shutil.rmtree(os.path.join(tempDir, 'AppModules'))


#清除app解压出来的_temp文件
clear_temp(r'%s' %(baseDir))
clear_temp(r'D:\servyou\QSHSQJ')

#copyUnsign2Sign()

#sigDll(version)

# upgrade文件夹下制作V1.1.012_V1.1.013.zip文件
makeUpgrade(preVersion, version)

#installsource文件夹下 制作jdls_NSGLWMH.dat
makeInstallsource(preVersion, version)
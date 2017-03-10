import os
import os.path
#print(dir(str))

dir=r"D:\servyou\NSGLWMH\V1.1.032\0000\installsource\jdls_NSGLWMH\AppModules\NSGLWMH\AppComs\a"
for path,dirnames,filenames in os.walk(dir):
	for filename in filenames:
		if   filename == 'sysconfig.ini':
			#os.remove(os.path.join(path, filename))
			print(os.path.relpath(path, r'D:\servyou\NSGLWMH\V1.1.032\0000\installsource\jdls_NSGLWMH\AppModules'))

for path,dirnames,filenames in os.walk(dir):
	for d in dirnames:
		#print(d)
		if len(os.listdir(os.path.join(path, d))) == 0:
			os.rmdir(os.path.join(path, d))
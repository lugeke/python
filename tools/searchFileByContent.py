import os
import fnmatch
def find_files(topdir, pattern):
	for path, dirname, filelist in os.walk(topdir):
		for name in filelist:
			#print(name)
			if fnmatch.fnmatch(name, pattern):
				yield os.path.join(path, name)

content = 'IsKjzf'
topdir = r'D:\servyou\NSGLWMH\V1.1.075\0000\installsource\jdls_NSGLWMH\AppModules\NSGLWMH\AppComs\Difference'

pattern = '*.xml'

def isTarget(file):
	if content == '':
		return False
	try:
		f = open(file)
		for  line in f:
			if content in line:
				print(line)
				return True
		else:
			return False
	except :
		print(file)
		

result = (list(filter(isTarget, find_files(topdir, pattern))))
for i in result:
	print(i)
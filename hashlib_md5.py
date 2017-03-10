import hashlib
import os, os.path

def CalcMD5(filepath):
	with open(filepath, 'rb') as f:
		m = hashlib.md5()
		m.update(f.read())
		return m.hexdigest()

dir = r'D:\servyou\downloads\201601\EPPortal_GS3.0-cq\AppModules\NSGLWMH\AppComs\Difference'

# for path,dirnames,filenames in os.walk(dir):
# 	for filename in filenames:
# 		if not filename.endswith('py'):
# 			print(filename + '-->' + CalcMD5(os.path.join(path, filename)))
# 	break

f = r'D:\servyou\Build\installer\SWYInst_09390100010000(国税税无忧工具箱).exe'
print(CalcMD5(f))
	
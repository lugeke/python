import sys, os, os.path
v2_dir = r'C:\Python27'
v3_dir = r'C:\Users\stay\AppData\Local\Programs\Python\Python35-32'

version = sys.version
if version.startswith("3") :
	os.rename(os.path.join(v3_dir,'python.exe'), os.path.join(v3_dir,'python3.exe'))
	os.rename(os.path.join(v2_dir,'python2.exe'), os.path.join(v2_dir,'python.exe'))
	print("python3->python2")
elif version.startswith("2"):
	os.rename(os.path.join(v2_dir,'python.exe'), os.path.join(v2_dir,'python2.exe'))
	os.rename(os.path.join(v3_dir,'python3.exe'), os.path.join(v3_dir,'python.exe'))
	print("python2->python3")

import zipfile
import os
#path = 'D:\python\servyou'


def zipDirs(*paths,**kwargs):
	zip_name = kwargs.get('zip_name','')
	if zip_name == '':
		zip_name = os.path.basename(paths[0])+'.zip'
	with zipfile.ZipFile(zip_name,'w')  as myzip:
		for path in paths:
			parentPath = os.path.dirname(path)
			for root, dirs, files in os.walk(path):
				myzip.write(root,os.path.relpath(root,parentPath))
				for f in files:
					myzip.write(os.path.join(root,f),os.path.relpath(os.path.join(root,f),parentPath))

zipDirs(r'D:\1',r'D:\2',r'E:\12\12',zip_name = 'a.zip')

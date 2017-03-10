import sys, configparser, os

baseurl = sys.argv[1]
if baseurl[-1] == '/':
	baseurl -= '/'

relative_path = sys.argv[2]
relative_path = '/'+relative_path

revision_start_int = sys.argv[3]
revision_end_int = sys.argv[4]

zip_name = os.path.basename(relative_path)
if len(sys.argv)==6:
	zip_name = sys.argv[5]
if not zip_name.endswith('.zip'):
	zip_name += '.zip'
zip_name = 'E:\\' + zip_name
print('zip_name'+zip_name)




# step 2: export file from revision_start to revision_end

import pysvn
#baseurl = 'https://192.168.31.225:8443/svn/ZZSNsgl/'
#relative_path = 'trunk/src/ZzsNgMain'
revision_start = pysvn.Revision(pysvn.opt_revision_kind.number, revision_start_int)
revision_end = pysvn.Revision(pysvn.opt_revision_kind.number, revision_end_int)

url = "%s%s" %(baseurl, relative_path)
#print(url)

client = pysvn.Client()
log_list = client.log(url,revision_start,revision_end,discover_changed_paths=True)

folderName = "E:\\svnFile"
if not os.path.exists(folderName):
    os.mkdir(folderName)


for log in log_list:
	#print(log.revision.number)
	for changed_path in log.changed_paths:
		#print("%s %s"%(changed_path.action, changed_path.path))
		if changed_path.path.startswith(relative_path):
			relpath = os.path.relpath(changed_path.path, relative_path)
			#print('relpath'+relpath)
			#print(changed_path.action+' '+relpath)
			dest_path = os.path.join(folderName, relpath)
			if changed_path.action == 'D':
				if os.path.exists(dest_path):
					if os.path.isfile(dest_path):
						os.remove(dest_path)
					elif os.path.isdir(dest_path):
						os.rmdir(dest_path)
			else:
				#print(baseurl+changed_path.path)
				os.makedirs(os.path.dirname(dest_path), exist_ok = True)
				#print('dest'+dest_path)
				#print(baseurl+'/'+changed_path.path)
				client.export(baseurl+changed_path.path, dest_path, True, revision=log.revision)


# step 3: compress dir

import zipfile, shutil
parent = folderName
#shutil.make_archive(zip_name,'zip','.',folderName)
with zipfile.ZipFile(zip_name, 'w') as myzip:
	
	for root, dirs, files in os.walk(folderName):
		if len(dirs)==0 and len(files)==0 and os.path.relpath(root, parent) != '.':
			myzip.write(root,os.path.relpath(root,parent))
		for f in files:
			myzip.write(os.path.join(root,f),os.path.relpath(os.path.join(root,f),parent))

shutil.rmtree(folderName)
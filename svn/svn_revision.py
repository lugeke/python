import sys, configparser, os


# step 1: read configure
try:
	configFile = open('config.ini','r')
except IOError:
	print('config.ini is not found')
	sys.exit()

config = configparser.ConfigParser()
config.read_file(configFile)
configFile.close()

try:
	baseurl = config.get('INFO', 'baseurl')
	if baseurl[-1] == '/':
		baseurl -= '/'
except configparser.NoOptionError:
	print('baseurl is not found under section INFO in config.ini')
	sys.exit()

try:
	relative_path = config.get('INFO', 'relative_path')
except configparser.NoOptionError:
	print('relative_path is not found under section INFO in config.ini')
	sys.exit()

try:
    revision_start_int = config.getint("INFO","revision_start")
except configparser.NoOptionError:
    print("revision_start is not found under section INFO in config.ini.")
    sys.exit()
try:
    revision_end_int = config.getint("INFO","revision_end")
except configparser.NoOptionError:
    print("revision_end is not found under section INFO in config.ini.")
    sys.exit()

zip_name = config.get('INFO', 'zip_name', fallback=os.path.basename(relative_path))
if not zip_name.endswith('.zip'):
	zip_name += '.zip'


# step 2: export file from revision_start to revision_end

import pysvn
#baseurl = 'https://192.168.31.225:8443/svn/ZZSNsgl'
#relative_path = '/trunk/src/ZzsNgMain'
revision_start = pysvn.Revision(pysvn.opt_revision_kind.number, revision_start_int)
revision_end = pysvn.Revision(pysvn.opt_revision_kind.number, revision_end_int)

url = "%s%s" %(baseurl, relative_path)
#print(url)

client = pysvn.Client()
log_list = client.log(url,revision_start,revision_end,discover_changed_paths=True)

folderName = "svnFile"
if not os.path.exists(folderName):
    os.mkdir(folderName)


for log in log_list:
	#print(log.revision.number)
	for changed_path in log.changed_paths:
		#print("%s %s"%(changed_path.action, changed_path.path))
		if changed_path.path.startswith(relative_path):
			relpath = os.path.relpath(changed_path.path, relative_path)
			#print(changed_path.action+' '+relpath)
			dest_path = os.path.join(folderName, relpath)
			if changed_path.action == 'D':
				if os.path.exists(dest_path):
					if os.path.isfile(dest_path):
						os.remove(dest_path)
					elif os.path.isdir(dest_path):
						os.rmdir(dest_path)
			else:
				os.makedirs(os.path.dirname(dest_path), exist_ok = True)
				client.export(baseurl+changed_path.path, dest_path, True, revision=log.revision)


# step 3: compress dir

import zipfile, shutil

# shutil.make_archive(zip_name,'zip','.',folderName)
with zipfile.ZipFile(zip_name, 'w') as myzip:
	parent = os.path.basename(folderName)
	for root, dirs, files in os.walk(folderName):
		if os.path.relpath(root, parent) != '.':
			myzip.write(root,os.path.relpath(root,parent))
		for f in files:
			myzip.write(os.path.join(root,f),os.path.relpath(os.path.join(root,f),parent))

shutil.rmtree(folderName)
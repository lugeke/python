import pysvn

url = 'https://192.168.31.225:8443/svn/ZZSNsgl/trunk/src/ZzsNgMain'
filename = 'f_view_sjcs.pas'


client = pysvn.Client()
log_list = client.log(url, discover_changed_paths=True)

find = False
for log in log_list:
	for changed_path in log.changed_paths:
		if changed_path.path.endswith(filename):
			author = log.author
			find = True
			break
	if find:break
print(author)
import os
dir=r"C:\Users\stay\Desktop\企业所得税年报报文"

for path,dirnames,filenames in os.walk(dir):
	for filename in filenames:
		if  filename.endswith('txt'):
			os.rename(os.path.join(path, filename), os.path.join(path, filename[:-3]+'xml'))
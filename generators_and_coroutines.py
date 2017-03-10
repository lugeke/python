import os 
import fnmatch

# the one with generators
def find_files(topdir, pattern):
	for path, dirname, filelist in os.walk(topdir):
		for name in filelist:
			if fnmatch.fnmatch(name,pattern):
				yield os.path.join(path,name)

import gzip, bz2
def opener(filenames):
	for name in filenames:
		if name.endswith(".gz"): 
			f = gzip.open(name)
		elif name.endswith(".bz2"):
			f= bz2.BZ2File(name)
		else:
			f = open(name)
		yield f

def cat(filelist):
	for f in filelist:
		for line in f:
			yield line

def grep(pattern, lines):
	for line in lines:
		if pattern in line:
			yield line

wwwlogs = find_files(r"D:\servyou\EPPortal_GS3.0\AppModules\ZZSNsgl\AppComs","*.xml")
files = opener(wwwlogs)
lines = cat(files)
pylines = grep("hdAuth",lines)
for line in pylines:
	#sys.stdout.write(line)
	print(line)


# the one with coroutine
def coroutine(func):
	def start(*args,**kwargs):
		g = func(*args,**kwargs)
		g.__next__()
		return g
	return start

@coroutine
def find_files(target):
	while True:
		topdir, pattern = (yield)
		for path, dirname, filelist in os.walk(topdir):
			for name in filelist:
				if fnmatch.fnmatch(name,pattern):
					target.send(os.path.join(path,name))

@coroutine
def opener(target):
	while True:
		name = yield
		if name.endswith(".gz"):
			f = gzip.open(name)
		elif name.endswith(".bz2"):
			f = bz2.BZ2File(name)
		else: 
			f = open(name)
		target.send(f)

@coroutine
def cat(target):
	while  True:
		f = (yield)
		for line in f:
			target.send(line)

@coroutine
def grep(pattern, target):
	while True:
		line = (yield)
		if pattern in line:
			target.send(line)

@coroutine
def printer():
	while True:
		line = (yield)
		sys.stdout.write(line)


# finder = find_files(opener(cat(grep("python", printer()))))
# finder.send(("www","access-log*"))
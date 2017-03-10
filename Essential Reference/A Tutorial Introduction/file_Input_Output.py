# file input
f = open("foo.txt")
line = f.readline()
while line:
	#print(line,end='')
	line = f.readline()
f.close()

#   file output 
year = 2015
f = open("out.txt",'w')
while year < 2050:
	#print("%3d" %(year),file=f)
	# f.wirte("%3d" %(year))
	year += 1
f.close()

#standard input output
import sys
#sys.stdout.write('Enter you name:')
#name = sys.stdin.readline()
name = input('Enter you name :')
content = '-->'
file = r'G:\PTXLocalMirror\{cf9e550b86f6e050a7faa810da961503}\LOG\日志_EPPortalnew_2016-01-20.LOG'
f = open(file)
for  line in f:
    if content in line:
        print(line)


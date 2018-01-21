import os, subprocess, shutil
import logging
# from shlex import quote
logging.basicConfig(filename='vps.log', format='%(asctime)s %(message)s', level=logging.INFO)

def normalize_dir(dir):
    basename = os.path.basename(dir)
    dirname = os.path.dirname(dir)
    os.rename(dir, os.path.join(dirname, basename.replace(' ', '_')))
# dirPath = r'H:\audiobook'
# for d in [f for f in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, f))]:
#     normalize_dir(os.path.join(dirPath, d))
# pscp -pw ~1%-ny5N2UGr  H:\\audiobook\\A_Short_History_Of_Nearly_Everything\\mylist.txt  jiaheng@97.64.29.113:/home/jiaheng/audio/temp
def scp(dir):
    src = dir
    des = r'/home/jiaheng/audio/temp'
    pwd = '~1%-ny5N2UGr'
    des = 'jiaheng@97.64.29.113:{}'.format(des)
    cmd = 'pscp -pw {} -r {}  {}'.format( pwd, src, des)
    print(cmd)
    os.system(cmd)

def generate_mp3_filelist(dirPath):
    listFile = os.path.join(dirPath, 'mylist.txt')
    if os.path.exists(listFile):
        print('mylist.txt exist')
        return
    files = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    files = [f for f in files if f.endswith('.mp3')]
    files.sort()
    if len(files) == 1:
        os.rename(os.path.join(dirPath, files[0]), os.path.join(dirPath, 'output.mp3'))
        print('only one file')
        return
    with open(listFile, 'w+') as lf:
        for f in files:
            fn = f.replace("'", "'\\''")
            lf.write('file \'{}\'\n'.format(fn) )    


dir = r'H:\audiobook\A_Short_History_Of_Nearly_Everything'

generate_mp3_filelist(dir)
# scp(dir)
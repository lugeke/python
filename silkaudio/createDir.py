import os, subprocess, shutil
import logging
# from shlex import quote
logging.basicConfig(filename='vps.log', format='%(asctime)s %(message)s', level=logging.INFO)

def format_audiobook(dirPath):
    hlsDir = os.path.join(dirPath, 'hls')
    if os.path.exists(hlsDir):
        logging.info('hls exist')
        return
    os.makedirs(hlsDir)
    files = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    
    for f in files:
        if f.endswith('.mp3'):
            # logging.info(os.path.join(path, f))
            chp_name = os.path.splitext(f)[0]
            book_name = os.path.basename(dirPath)
            
            chp_dir = os.path.join(hlsDir, chp_name)
            shutil.rmtree(chp_dir, ignore_errors=True)
            os.makedirs(chp_dir)
            subprocess.call(['/usr/local/bin/mediafilesegmenter', 
                            # '-b',  '/audiobook/{}/{}'.format(book_name, chp_name),
                            '-t', '60', # duriation
                            '-f', chp_dir, # filepath
                            os.path.join(dirPath, f)])
        


def generate_chps_json(dirPath):
    result = []
    files = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    for f in files:
        if f.endswith('.mp3'):
            result.append(f[:-4])
        if f.endswith('.jpg') and f != 'cover.jpg':
            os.rename(os.path.join(dirPath, f), os.path.join(dirPath, 'cover.jpg'))
            logging.info('{}->cover.jpg'.format(f))
    result.sort()
    import json
    with open(os.path.join(dirPath, 'chps.json'),'w') as f:
        json.dump(result, f)



def uploadHls(dir):
    # change to current Dir
    os.system('cp ./silkaudio/s4.sh {}/upload.sh'.format(dir))
    os.chdir(dir)
    logging.info('chdir '+dir)
    bookName = os.path.basename(dir)
    logging.info('book '+ bookName)
    serverBookDir = os.path.join('/home/jiaheng/audio', bookName)
    
    with open('upload.sh', 'a') as f:

        logging.info(serverBookDir)
        tarFile = 'hls.tar.gz'
        ip = '97.64.29.113'
        user = 'jiaheng'

        s0 = 'cd {} && cp ./book.json ./chps.json ./cover.jpg ./hls'.format(dir)
        print('s0 ', s0)
        f.write(s0+' && echo s0done && ')
        
        # tar hls: tar -zcvf hls.tar.gz dir/hls
        s1 = 'tar -zcf hls.tar.gz hls'
        print('s1 ', s1)
        f.write(s1+' && echo s1done && ')
        # mkdir 

        
        s2 = 'ssh {}@{} "mkdir -p {}"'.format(user, ip, serverBookDir) 
        print('s2 ', s2)
        f.write(s2+' && echo s2done && ')

        # upload
        s3 = 'scp -p {} {}@{}:{}'.format(os.path.join(dir, tarFile) , user, ip, serverBookDir)
        print('s3 ', s3)
        f.write(s3+' && echo s3done && ')

        s4 = 'ssh {}@{} "cd {} && tar -xzf {} --strip 1 && rm -f {} && chmod -R 755 {}  "'.format(
                        user, ip, serverBookDir, tarFile, tarFile, serverBookDir)
        print('s4 ', s4)
        f.write(s4+' && echo s4done ') 

    

# dirPath = r'/Users/lugeke/Desktop/audiobook/'
# dirs = [f for f in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, f))]
# for d in dirs:
#     # generate_chps_json(os.path.join(dirPath, d))
#     logging.info('\n process dir ' + d)
#     format_audiobook(os.path.join(dirPath, d))
#     uploadHls(os.path.join(dirPath, d))


dir = r'/Users/lugeke/Desktop/audiobook/The_Martian'
format_audiobook(dir)
generate_chps_json(dir)
uploadHls(dir)
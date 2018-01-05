from threading import Thread
from queue import Queue
import time
import os
import logging
import re
import concurrent.futures
#filename='upload.log'
logging.basicConfig( format='%(asctime)s %(message)s', level=logging.DEBUG)
queue = Queue(5)
close = False
filenames = ['xart.17.06.30.jenna.and.kenna.james.xxx.threeway.games.mp4', 
'agm.17.01.02.kimmy.granger.and.lyra.law.surrender.your.stress.mp4',
'agm.17.01.02.kimmy.granger.surrender.your.stress.mp4'
]

filenameSet = set() 
def scanDir(dirPath):
    while not close:
        for path,dirnames,filenames in os.walk(dirPath):
            for f in filenames:
                if f not in filenameSet:
                    extName = os.path.splitext(f)[1]
                    if extName in {'.mp4', '.wmv', '.avi', '.mkv'}:
                        filenameSet.add(f)
                        queue.put({
                            'filename': f,
                            'path': path
                        })
                        logging.info('queue put {} success'.format(f))
                    
        logging.info('-')
        time.sleep(30)


def generateUploadInfo(filename):
    # regex = re.compile(r'(\w+)(?:\.\d\d){3}\.(.+?xxx|\w+\.\w+)(.+)?\.\w{3}')
    regex = re.compile(r'(\w+)(?:\.\d\d){3}\.((?:\w+\.and\.\w+\.\w+)|(?:\w+\.\w+\.and\.\w+\.\w+)|(?:\w+\.\w+)).+')
    match = regex.search(filename)
  
    if match:
        studio, actors = match.groups()
        actors = actors.strip('.').split('and')
        actors = ' '.join(['&nbsp;'.join(n.strip('.').split('.')) for n in actors])
        
        title = filename[:-4]
        tags = '{} {}'.format(studio, actors)
        logging.info(tags)
        return (title, tags)
    else:
        logging.info('no match for {}'.format(filename))
    
    
# for f in filenames:
#     generateUploadInfo(f)

def uploadFile():
    fileInfo = queue.get()
    
    filename = fileInfo['filename']
    logging.info('process {}'.format(filename))
    filepath = os.path.join(fileInfo['path'], filename)
    # title, tags = generateUploadInfo(filename)
    logging.info('')
    time.sleep(10)
    logging.info('process {} done.'.format(filename))

def runThreadPool(dirPath):
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its index
        executor.submit(scanDir, dirPath)
        while not close:
            future_to_index = {executor.submit(uploadFile): i for i in range(3)}
            
            for future in concurrent.futures.as_completed(future_to_index):
                f = future_to_index[future]
    
if __name__ == '__main__': 
    dirPath = r'/Users/lugeke/Downloads' 
    runThreadPool(dirPath)
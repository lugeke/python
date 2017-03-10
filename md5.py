import os.path
from hashlib import md5

def md5_file(name):
    if os.path.isfile(name):
        m = md5()
        a_file = open(name, 'rb')    #��Ҫʹ�ö����Ƹ�ʽ��ȡ�ļ�����
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()
    else:
        return ""
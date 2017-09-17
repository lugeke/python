import bencode
import hashlib
import base64
import os


def hash(f):
    torrent = open(f, 'rb').read()
    metadata = bencode.bdecode(torrent)
    hashcontents = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest)
    print('magnet:?xt=urn:btih:'+b32hash)


dir = r'/Users/lugeke/Downloads/bt'
f_list = []
h_list = []
for path, dirnames, filenames in os.walk(dir):
    print(filenames)
    for f in filenames:
        f = os.path.join(path, f)
        f_list.append(f)

print(len(f_list))

for f in f_list:
    h_list.append(hash(f))
print(len(h_list))
import os
path = r'D:\python\servyou'

print(os.path.abspath(path))
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.relpath(path,os.path.dirname(path)))

os.path.relpath(r'f:\a\b\1.txt', r'f:\a')



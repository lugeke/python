import os
import os.path
import codecs
import tempfile
import re

zhPattern = re.compile(u'[\u4e00-\u9fa5]')

dir = r"G:\BaiduYunDownload\subtitles"

for path,dirnames,filenames in os.walk(dir):
	for filename in filenames:
		if  filename.endswith('srt'):
			
			t = tempfile.NamedTemporaryFile(mode = 'r+')
			f = codecs.open(os.path.join(path, filename), 'r', 'utf-8')
			try:
				for line in f:
					if (not zhPattern.search(line)) and (line.strip() != ''):
						t.write(line + '\n')
			except:
				print(filename+ ' '+ line)
			f.close()

			t.seek(0)
			f = codecs.open(os.path.join(path, filename), 'w', 'utf-8')
			for line in t:
				f.write(line)
			t.close()
	break



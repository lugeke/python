import xml.etree.ElementTree as ET

try:
	treeBing = ET.parse('bingDict.xml')
	treeYoudao = ET.parse('123.xml')
	root = treeBing.getroot()
	wordbook = treeYoudao.getroot()
except :
	print('parse error')
	exit(0)

for phrase in root[0].findall('Phrase'):
	item = ET.Element('item')
	word = ET.SubElement(item, 'word')
	trans = ET.SubElement(item, 'trans')
	phonetic = ET.SubElement(item, 'phonetic')
	tags = ET.SubElement(item, 'tags')
	progress = ET.SubElement(item, 'progress')
	print(phrase.find('Eng').text )
	word.text = phrase.find('Eng').text 
	trans.text = phrase.find('Defi').text 
	progress.text = '1'

	wordbook.append(item)
treeYoudao.write('output.xml', 'utf-8')
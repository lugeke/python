import xml.etree.ElementTree as ET

try:
	node = ET.parse(r'D:\python\servyou\nodes.xml')
except Exception as e:
	print(e)
	exit(0)


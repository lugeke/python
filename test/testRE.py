import re

def test_match1():
	size = '343333'
	pattern = re.compile(r'(\d)\1{2,5}|(\d)\d\1{2,4}')
	#match = pattern.findall(size)
	match = pattern.match(size)
	if match:
		print('true')
		# size = float(match.group(1))
		# if match.group(2) == 'MB':
		# 	size /= 1024
test_match1()
def test_match():
	size = 'Size:932.23MB / Convert Date:2015-07-26 12.34GB  12.9gba 13.4gb,'
	pattern = re.compile(r'\b(\d+\.?\d*)([GgMm][Bb])\b')
	#match = pattern.findall(size)
	match = pattern.match(size)
	if match:
		print(match)
		# size = float(match.group(1))
		# if match.group(2) == 'MB':
		# 	size /= 1024
#test_match()

def test_sub():
	text = 'Game of Thrones'
	print(re.sub(r'\s+', '-', text))
	print(re.sub(r'\w+', lambda m:'[' + m.group(0) + ']', text, 0))
#test_sub()



def test_zerowidth():
	#给一个很长的数字中每三位间加一个逗号(当然是从右边加起了)
	text = '   1234512134mmmm'
	print(re.findall(r'(\d)(?=(\d{3})+(?!\d))', text))
	print(re.sub(r'(\d)(?=(\d{3})+(?!\d))', lambda m: m.group(1)+',', text))

def test():
	dailybugle = 'Spider-Man Menaces City!'
	pattern = r'spider[- ]?man.'
	if re.match(pattern, dailybugle, re.IGNORECASE):
		print(dailybugle)


	date = '12/30/1969'
	regex = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(?:\d\d)?)$')
	match = regex.match(date)
	if match:
		print(match.group(1))
		print(match.group(2))
		print(match.group(3))


#test()
def search(pattern, text):
	'Return True if pattern appears anywhere in text.'
	if pattern.startswith('^'):
		return (match(pattern[1:], text))
	else:
		return match('.*' + pattern, text)

def match(pattern, text):
	'Return True if pattern appears at the start of text.'
	if pattern == '':
		return True
	elif pattern == '$':
		return text == ''
	elif len(pattern) > 1 and pattern[1] in '*?':
		
	else:
		return (match1(pattern[0], text) and
			match(pattern[1:], text[1:])
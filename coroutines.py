import types
def grep(pattern):
	print('Searching for', pattern)
	while  True:
		line = (yield)
		if pattern in line:
			print(line)


search = grep('coroutine')
print(type(search))
next(search)
search.send('I do love you')
search.send("Don't you love me")
search.send('I love coroutine')
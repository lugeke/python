stock = {
	'name' : 'GOOD',
	'shares' : 100,
	'price' : 490.10
}

print(stock)
name = stock['name']
print(name)

# insert or modify dict
stock['shares'] = 75
stock['date'] = 'June 7, 2015'
print(stock)

# empty dict
princes = {}
princes = dict()

# get a value
s = stock.get('name','IBM')
print(s)

# iterate a dict
for key in stock:
	print(key, stock[key])
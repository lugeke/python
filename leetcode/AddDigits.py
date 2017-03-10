def addDigits(num):
	while num >= 10 :
		x = num
		s = 0
		while x != 0:
			s += x % 10
			x //= 10
		num =s
	return num

print(addDigits(10))
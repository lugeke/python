from functools import lru_cache

from decorators import clock
@clock
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)
 

fib(10)
print('---->')


@lru_cache()
@clock
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

fib(10)
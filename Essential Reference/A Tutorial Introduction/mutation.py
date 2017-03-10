def add_to(num, target=[]):
	target.append(num)
	return target

print(add_to(1))

print(add_to(2))

print(add_to(3))

#  Well again it is the mutability of lists which causes this pain. 
#  In Python the default arguments are evaluated once when the function is defined, 
#   not each time the function is called. 
#  You should never define default arguments of mutable type unless you know what you are doing

def add_to(element, target=None):
	if target is None:
		target = []
	target.append(element)
	return target


print(add_to(1))
print(add_to(2))
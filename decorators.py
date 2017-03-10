def a_new_docorator(func):

	def wrapTheFunction():
		print("I am doing some boring work before executing func")
		func()
		print("I am doing some boring work after executing func")
	return wrapTheFunction

def function_requiring_decoration():
	print("I am the function which needs some decoration to remove my foul smell")

function_requiring_decoration()

function_requiring_decoration = a_new_docorator(function_requiring_decoration)

function_requiring_decoration()


@a_new_docorator
def function_requiring_decoration():
	print("I am the function which needs some decoration to remove my foul smell")

function_requiring_decoration()
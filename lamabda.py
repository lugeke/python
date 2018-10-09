def multipliers():
    return [lambda x: i*x for i in range(4)]



print([m(2) for m in multipliers()])


# Python’s closures are late binding. This means that the values of 
# variables used in closures are looked up at the time the inner function is called.

# functions created with a lambda expression are in no way special, 
# and in fact the same exact behavior is exhibited by just using an ordinary def
def multipliers():
    multipliers = []

    for i in range(4):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)

    return multipliers
print([m(2) for m in multipliers()])

# solution
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]

print([m(2) for m in multipliers()])

def multipliers():
    for i in range(4):
        yield lambda x: i * x

print([m(2) for m in multipliers()])


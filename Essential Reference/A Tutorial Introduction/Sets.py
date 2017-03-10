s = set([3,5,9,10])
t = set('Hello')
print(t)

# Union of t and s
a = t | s
print(a)
# Intersection of t and s
b = t & s
print(b)
# Set difference(items in t, but not in s)
c = t - s
print(c)
# Symmetric difference (items in t or s, but not both)
d = t ^ s
print(d)

t.remove('H')
print(t)
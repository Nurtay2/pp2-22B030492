x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

x1 = 1    # int
y1 = 2.8  # float
z1 = 1j   # complex

#convert from int to float:
a = float(x1)

#convert from float to int:
b = int(y1)

#convert from int to complex:
c = complex(x1)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1, 10))
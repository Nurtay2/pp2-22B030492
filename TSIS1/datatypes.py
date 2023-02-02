# x = "Hello World"	str
# x = 20	int
# x = 20.5	float
# x = 1j	complex
# x = ["apple", "banana", "cherry"]	list
# x = ("apple", "banana", "cherry")	tuple
# x = range(6)	range
# x = {"name" : "John", "age" : 36}	dict
# x = {"apple", "banana", "cherry"}	set
# x = frozenset({"apple", "banana", "cherry"})	frozenset
# x = True	bool
# x = b"Hello"	bytes
# x = bytearray(5)	bytearray
# x = memoryview(bytes(5))	memoryview
# x = None	NoneType

x = str("Hello World")	#str
y = int(20)	#int
z = float(20.5)	#float
a = complex(1j)	#complex
b = list(("apple", "banana", "cherry"))	#list
c = tuple(("apple", "banana", "cherry"))	#tuple
d = range(6)	#range
e = dict(name="John", age=36)	#dict
f = set(("apple", "banana", "cherry"))	#set
g = frozenset(("apple", "banana", "cherry"))	#frozenset
h1 = bool(5)	#bool
h = bytes(5)	#bytes
h2 = bytearray(5)	#bytearray
j = memoryview(bytes(5))	#memoryview

#exercices
x1 = 5
print(type(x))

y1 = "Hello World"
print(type(y))

z1 = 20.5
print(type(z))

l = ["apple", "banana", "cherry"]
print(type(l))

m = ("apple", "banana", "cherry")
print(type(m))

n = {"name" : "John", "age" : 36}
print(type(n))

o = True
print(type(o))
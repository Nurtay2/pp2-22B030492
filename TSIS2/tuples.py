#TUPLES
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  #ordered, unchangable, allow duplicates
print(len(thistuple))
print('\n')

thistuple2 = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple3 = ("apple")
print(type(thistuple))
print('\n')

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple4 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple4)



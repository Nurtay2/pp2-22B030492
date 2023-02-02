#SETS
#A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset2 = {"apple", "banana", "cherry", "apple"}

print(thisset2) #duplicates not allowed
print(len(thisset2))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset3 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset3)


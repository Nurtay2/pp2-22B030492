a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

c = 2
d = 330
print("A") if c > d else print("B")

a1 = 200
b1 = 33
c1 = 500
if a1 > b1 and c1 > a1:
  print("Both conditions are True")
elif a1 > b1 or a1 > c1:
  print("At least one of the conditions is True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a2 = 33
b2 = 200

if b2 > a2:
  pass
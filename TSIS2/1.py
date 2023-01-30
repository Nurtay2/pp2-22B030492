i = 1
while i < 6:
  print(i)
  i += 1
print('\n')
j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1
print('\n')
a = 0
while a < 6:
  a += 1
  if a == 3:
    continue
  print(a)
print('\n')
b = 1
while b < 6:
  print(b)
  b += 1
else:
  print("i is no longer less than 6")
def Even_num(n):
    for i in range(n):
        if i%2 == 0:
            yield i
n = int(input("Enter the number: "))
s = []
for i in Even_num(n):
    s.append(i)
print(*s, sep = ", ")
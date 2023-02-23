def Even_num(n):
    for i in range(n):
        if i%3 == 0 and i%4 == 0:
            yield i
n = int(input("Enter the number: "))
for i in Even_num(n):
    print(i)
def squares(n):
    for i in range(n):
        yield i*i
n = int(input("Enter the number: "))
for i in squares(n):
    print(i)

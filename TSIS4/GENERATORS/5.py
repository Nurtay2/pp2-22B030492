def Down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter the number: "))
for i in Down(n):
    print(i)
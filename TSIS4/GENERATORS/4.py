def Squares(a, b):
    for i in range(a, b):
        yield i*i
a, b = int(input("Enter the first number: ")), int(input("Enter the second number: "))
for i in range(a, b):
    for j in Squares(a, b):
        if i*i == j:
            print(j)
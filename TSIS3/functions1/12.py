def histogram(l:list):
    for i in l:
        print("*"*i)
l = [int(x) for x in input().split()]
histogram(l)
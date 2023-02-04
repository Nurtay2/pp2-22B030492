def unique(l:list):
    unique_l = []
    for i in l:
        if i not in unique_l:
            unique_l.append(i)
    print(unique_l)
l = [int(x) for x in input().split()]
unique(l)
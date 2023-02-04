def has_33(l:list):
    s = ""
    for i in range(len(l)):
        s+=str(l[i])
    if s.find('33') + 1 > 0:
        print("True")
    else:
        print("False")

l = [int(x) for x in input().split()]
has_33(l)

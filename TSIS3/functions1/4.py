def filter_prime(c):
    ok = True
    for i in range(2, c):
        if c % i == 0:
            ok = False
            break
    return ok


if __name__ == "__main__":
    a =  int(input())
    l = []
    for i in range(a):
        c = int(input())
        if filter_prime(c):
            l.append(c)
    print(l)


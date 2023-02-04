def filter_prime(it:list):
    prime = []
    for i in range(len(it)):
        for j in range(2, it[i]):

            if it[i]%j==0:
                break
            else:
                prime.append(it[i])
        else:
            continue
    print(set(prime))
it = [1,2,3,4,5,6,7,8,9,10,11,12,13, 15, 16, 17 ,18, 20, 23, 24]
filter_prime(it)


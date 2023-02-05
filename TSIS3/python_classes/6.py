import random
class Filter:
    def __init__(self, num):
        self.num = num

    def filter_prime(self, num):
        ok = True
        for i in range(2, self.num):
            if self.num == 1:
                ok = False
                break
            elif self.num % i == 0:
                ok = False
                break
        return ok
b = int(input("Enter the amount of number: "))
list1 = []
for i in range(b):
    k = int(input())
    n = random.randint(1, 15)
    #print(n)
    x = lambda k, n : k + n
    list1.append(x(k, n))
print(list1)
list2 = []
for i in list1:
    j = Filter(i)
    if j.filter_prime(j):
        list2.append(i)
print(list2)

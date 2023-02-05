class Account:
    def __init__(self, facilities):
        self.facilities = facilities
    def get_facilities(self):
        return self.facilities

    def deposit(self, n):
        global x
        x = self.facilities
        x = x + n
        return x
    def withdraw(self, n):
        global y
        y = self.facilities
        y = y - n
        return y

deposit1 = Account(0)
deposit2 = Account(0)

a = input("Choose the owner: [Nurzhan] or [Olzhas]  ")

if a == "Nurzhan":
    print("if you want to deposit money: input DEP")
    print("if you want to withdraw money: input WITH")
    print("if you want to stop: input NO")
    while deposit1.get_facilities() >= 5000 or deposit1.get_facilities() <= 1000:
        c = input()
        if c == "DEP":
            n = int(input())
            print(deposit1.deposit(n))
        elif c == "WITH":
            n = int(input())
            print(deposit1.withdraw(n))
        elif c == "NO":
            break






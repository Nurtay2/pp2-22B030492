def solve(numlegs, numheads):
    Y = int((numlegs - 2*numheads)/2)
    X = int(numheads - Y)
    print("num of rabbits:", Y)
    print("num of chickens:", X)
numheads, numlegs = int(input("num of heads: ")), int(input("num of legs: "))
solve(numlegs, numheads)
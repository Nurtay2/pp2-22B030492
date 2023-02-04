from itertools import permutations
def perm(s):
    per = permutations(s)
    for i in list(per):
        print("".join(i))
if __name__ == "__main__":
    s = input("Enter the word: ")
    perm(s)
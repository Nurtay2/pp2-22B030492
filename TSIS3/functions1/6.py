def reverse_sentences(s):
    res = s.split()
    res.reverse()
    s2 = ""
    for i in res:
        s2 = s2 + i + " "

    print(s2)
s = input("Enter the sentences: ")
reverse_sentences(s)
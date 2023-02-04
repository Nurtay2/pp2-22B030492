def palindrome(s):
    s2 = s[::-1]
    if s2 == s:
        print("This word is palindrome")
    else:
        print("Not palindrome")
s = input("Enter the word: ")
palindrome(s)
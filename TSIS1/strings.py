a = "Hello"
print(a)


b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)  #multiline string

c = "Hello, World!"
print(c[1]) #strings are arrays
for i in c:
    print(i)
print(len(c))

txt = "The best things in life are free!"
print("free" in txt) #true
print("expensive" not in txt) #true
if "free" in txt:
  print("Yes, 'free' is present.")
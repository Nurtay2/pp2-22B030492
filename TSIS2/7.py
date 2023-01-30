#DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])


thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020  #duplicates not allowed
}
print(thisdict2)
print(len(thisdict2))

thisdict3 = {
  "brand": "Ford",
  "electric": False, #it can be any data type
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict3))

thisdict4 = dict(name = "John", age = 36, country = "Norway")
print(thisdict4)



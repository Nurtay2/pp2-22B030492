import os
items = ['Nurzhan ', 'is ', 'strong ', 'person ', 'and ', 'very ', 'clever  ', 'man ']
file = open('../5.txt', 'w')
file.writelines(items)
file.close()
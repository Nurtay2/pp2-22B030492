import os
def createFile(f):
    for i in f:
        i = open(f+".txt", 'w+',)
f = '[a - z]'
createFile(f)
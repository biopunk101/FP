#write txt file

import os

filename = 'd:/Workbench/pycode/fp/log.txt'
f = open(filename, 'w')

for i in range(10):
    print('write data line: ', i, file = f)
    #f.write("write data line: ")

f.close()
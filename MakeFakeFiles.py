import shutil
import os
from os import walk
from os.path import join

MyPath = 'D:/temp/'
listFile = MyPath + 'list.txt'

f = open(listFile, 'r')
files = f.readlines()

for i in files:
    #print(i)
    str = i
    fileName = str.strip('\n')
    if i not in os.listdir(MyPath):
        tmp = open(MyPath + fileName, 'w')
        tmp.close()


f.close()
import os
from os import walk
from os.path import join

DestPath = 'D:/temp/'

f = open('D:/temp/list.txt', 'w')

for SrcPath, dirs, files in walk(DestPath):
    for i in files:
        FullPath = join(SrcPath, i) # 獲取檔案完整路徑
        FileName = join(i) # 獲取檔案名稱
        print (FullPath, file = f)
        #print (FileName)



f.close()
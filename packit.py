#符合檔案關鍵字 新增關鍵字資料夾並移動

import shutil
import os
from os import walk
from os.path import join


HomePath = '//192.168.11.100/home/'
MPath = '//192.168.11.100/home/EROMA/'

print('輸入檔案關鍵字: ')
tar = input()

TarPath = MPath+tar+'/'
AllFiles = os.listdir(MPath)

#print(AllFiles)

MatchCnt = 0
count = 0

for i in AllFiles:
    FullPath = MPath + '/' + i
    #print(FullPath)
    FileName = i
    #print(FileName)
    if tar in FileName:
        if not os.path.exists(TarPath):
            os.mkdir(TarPath)
        shutil.move(FullPath, TarPath)
        print('將', FileName, '移動至' , tar, '資料夾')
        MatchCnt = MatchCnt + 1

print('Move ', MatchCnt, 'File to directory.')    

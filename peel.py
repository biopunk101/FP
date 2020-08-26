#針對目標路徑分析 將路徑內資料夾中檔案移出至目標路徑
import shutil
import os
from os import walk
from os.path import join


#print('輸入來源資料夾路徑:')
#SrcPath = input()
MyPath = 'D:/temp/'
LogPath = MyPath + 'log.txt'

f = open(LogPath, 'w')

#print('輸入目的資料夾路徑:')
#TarPath = input()
DestPath = MyPath


for SrcPath, dirs, files in walk(MyPath):
  for i in files:
    #FullPath = SrcPath + i # 獲取檔案完整路徑
    FullPath = join(SrcPath, i) # 獲取檔案完整路徑
    FileName = join(i) # 獲取檔案名稱
    #print (FullPath)
    #print (FileName)
    if not os.path.exists(MyPath+'/'+FileName):
        shutil.move(FullPath, DestPath)
        print('將', i, '移動至資料夾:',DestPath, file = f )
    else:
        print(i, '已存在於資料夾:',DestPath, file = f )

f.close()



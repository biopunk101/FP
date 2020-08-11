#檔案名稱符合關鍵字 將檔案移動至關鍵字資料夾

import shutil
import os
from os import walk
from os.path import join

MyPath  = 'D:/temp' # 當下目錄
#DestPath = 'D:/temp'
#SrcPath = 'D:\temp'
print('請輸入檔案關鍵字:')
KEYWORD = input()

for SrcPath, dirs, files in walk(MyPath):
  for i in files:
    FullPath = join(SrcPath, i) # 獲取檔案完整路徑
    FileName = join(i) # 獲取檔案名稱
    DestPath = (MyPath +'/'+ KEYWORD)
    #print (FullPath)
    #print (FileName)

    if KEYWORD in FileName:
      if not os.path.exists(MyPath +'/'+ KEYWORD +'/'+ FileName):
        if not os.path.exists(DestPath):
          os.mkdir(MyPath+'/'+KEYWORD)
          print ('建立 "'+KEYWORD+'" 資料夾...')
        shutil.move(FullPath, MyPath+'/'+KEYWORD)
        print ('成功將', FileName, '移動至', KEYWORD, '資料夾')
      else :
        print (FileName, '已存在，故不執行動作')
    else:
      print(FileName, '檔案不符合關鍵字', KEYWORD)




# for root, dirs, files in walk(MyPath):
#   for i in files:
#     FullPath = join(root, i) # 獲取檔案完整路徑
#     FileName = join(i) # 獲取檔案名稱
#
#     if xx in FullPath:
#       if not os.path.exists(MyPath + '/' + xx + '/' + FileName):
#         if not os.path.exists(xx):
#           os.mkdir(xx)
#         #shutil.move(FullPath, MyPath + '/' + xx)
#         print (FullPath)
#         #print ('成功將', FileName, '移動至', xx, '資料夾')
#       else:
#         print (FileName, '已存在，故不執行動作')
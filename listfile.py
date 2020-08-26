import shutil
import os
import glob
from os import walk
from os.path import join

Path = '../../Download/'
#MyPath = 'D:/temp/'
print('Input the path of target direcory:')
x = raw_input()
MyPath = Path + x + '/'

LogPath = MyPath + 'list.txt'
DestPath = MyPath

print ('Target directory: ', MyPath)
print ('input Y to continue...')
str = raw_input()

if str == 'Y':
  f = open(LogPath, 'w')
  for SrcPath, dirs, files in walk(MyPath):
    for i in files:
      if '.avi' in i:
        if 's800' not in i:
          if 's100' not in i:
             if 'default' not in i:
                if 'a100' not in i:
                    tmp = i + '\n'
                    f.writelines(tmp)
      elif '.mp4' in i:
        if 's800' not in i:
            if 's100' not in i:
                if 'default' not in i:
                    if 'a100' not in i:
                        tmp = i + '\n'
                        f.writelines(tmp)

  f.close()
else:
  exit()


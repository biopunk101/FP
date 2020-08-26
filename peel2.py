import shutil
import os
from os import walk
from os.path import join

Path = '../../Download/'
#MyPath = 'D:/temp/'
print('Input the path of target direcory:')
x = raw_input()
MyPath = Path + x + '/'
#MyPath = x

LogPath = MyPath + x + 'log.txt'
DestPath = MyPath

print ('Target directory: ', MyPath)
print ('input Y to continue...')
str = raw_input()

if str == 'Y':
  f = open(LogPath, 'w')
  for SrcPath, dirs, files in walk(MyPath):
    for i in files:
      #FullPath = SrcPath + i #get the full path
      FullPath = join(SrcPath, i) # get file full path
      FileName = join(i) #get file name
      #print (FullPath)
      #print (FileName)
      if not os.path.exists(MyPath+'/'+FileName):
          shutil.move(FullPath, DestPath)
          #print('Move', i, 'to directoty:',DestPath, file = f )
          tmp = 'Move' + i + 'to directory:' + DestPath + '\n'
          f.writelines(tmp)
      else:
          #print(i, 'Already has:',DestPath, file = f )
          tmp = 'Already has' + i + '\n'
          f.writelines(tmp)

  f.close()
else:
  exit()


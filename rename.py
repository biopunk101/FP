#rename
import os

MyPath = 'D:/NTA/NTA/'

str1 = '['
str2 = '_ch'
str3 = '_sub'
str4 = 'r.'

for i in os.listdir(MyPath):
    #tmp = print(i)
    tmp = i
    if str1 in i:
        tmp = tmp.replace('[', '')
        if not os.path.exists(MyPath+tmp):
            os.rename(MyPath+i, MyPath+tmp)
    elif str2 in i:
        tmp = tmp.replace(str2, '')
        if not os.path.exists(MyPath+tmp):
            os.rename(MyPath+i, MyPath+tmp)
    elif str3 in i:
        tmp = tmp.replace(str3, '')
        if not os.path.exists(MyPath+tmp):
            os.rename(MyPath+i, MyPath+tmp)
    elif str4 in i:
        tmp = tmp.replace(str4, '.')
        if not os.path.exists(MyPath+tmp):
            os.rename(MyPath+i, MyPath+tmp)













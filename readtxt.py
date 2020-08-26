import os

#home = os.getcwd()
#home = __file__
#print(home)

# 讀取檔案內容行數
f = open("d:/Workbench/pycode/fp/path.txt", "r")
lines = f.readlines()
print(len(lines))
f.close()

# wd = os.getcwd()
# print("working directory is ", wd)
#
# filePath = __file__
# print("This script file path is ", filePath)
#
# absFilePath = os.path.abspath(__file__)
# print("This script absolute path is ", absFilePath)
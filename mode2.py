import os
import shutil
import pandas as pd

def mkdirs(path):
    path = path.strip()
    path = path.rstrip("\\") # 去除尾部 \ 符號
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)         # 建立目錄
        print(path + ' 建立成功')
        return True
    else:
        print(path + ' 目錄已存在')
        return False

'''將原根目錄路徑下所有子檔案移動到新資料夾中,分類依據為檔名稱包含資料夾名稱'''
def search_file(row_root_path, foldername, new_root_path):
    queue = []
    queue.append(row_root_path)
    while len(queue) > 0:
        tmp = queue.pop(0)
        if (os.path.isdir(tmp)):  #如果該路徑是資料夾,遍歷該路徑中檔案和資料夾
            for item in os.listdir(tmp):
                queue.append(os.path.join(tmp, item))  # 將所得路徑加入佇列queue
        elif (os.path.isfile(tmp)): #如果該路徑是檔案,獲取檔名和檔案目錄，將檔名與檔案目錄連線起來，形成完整路徑
            name = os.path.basename(tmp)
            dirname = os.path.dirname(tmp)
            row_full_path = os.path.join(dirname, name)
            new_full_path = new_root_path +'/' + name #定義新路徑，匹配符合條件的檔案
            if foldername in name:
                shutil.move(row_full_path, new_full_path)

if __name__ == '__main__':
    data=pd.read_excel('D:/movelist.xlsx') #檔案批量分類到資料夾
    for i in data['dir']:
        mkdirs(i)
    for i in range(len(data['type'])):
        search_file(data['resource'][i],data['type'][i].strip(),data['dir'][i])
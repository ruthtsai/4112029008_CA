import os
import shutil
import time


#1.建立名為CS的目錄

os.mkdir("CS")

#2.在CS目錄下建立一個名為homework的txt檔
#3.在txt檔寫入內容(內容為：自己的學號_名字)

file_HW = os.path.join("CS", "homework.txt")
with open(file_HW, "w") as file:
    file.write("4112029008_蔡侑容\n")
    
#4.讀資料內容跟檔案資訊

file = open("CS\homework.txt","r")
file_content = file.read()
print(f'檔案內容為：{file_content}')

#文件大小(以字節為單位)
file_size = os.path.getsize("CS\homework.txt")
print(f'文件大小：{file_size}字節')

#最後修改時間(時間戳)
modificatiom_time = os.path.getmtime("CS\homework.txt")
print(f'最後修改時間：{modificatiom_time}')

#將時間戳改為人類可讀模式
formatted_time = time.ctime(modificatiom_time)
print(f'最後修改時間 ( 人類可讀格式 )：{formatted_time}')

file.close()

#5.刪除檔案與目錄
#刪除檔案
if os.path.exists("CS\homework.txt"):
    os.remove("CS\homework.txt")
    
os.rmdir("CS")

print("目錄與檔案已刪除")    



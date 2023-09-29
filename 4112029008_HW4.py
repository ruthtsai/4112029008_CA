'''
建立一個名為 BBQ 的資料庫，內有名為 meat 的表格
含四個欄位 id(PK), name, price, quantity
資料型態分別為 INTEGER, TEXT, INTEGER, INTEGER
'''

import sqlite3


#連結到 SQlite3 資料庫(如果不存在，將創建一個新的資料庫文件)
conn = sqlite3.connect("BBQ.db")

#創建一個游標對象，用於執行 SQL 查詢
cursor = conn.cursor()

#創建名為"meat"的表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )''')
    
#插入資料 增加三筆資料
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES('chicken', 30, 5)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES('beaf', 55, 10)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES('pork', 40, 15)")
#提交事務
conn.commit()

cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("肉類清單：")
for kind in meat:
    print(kind)
    
#更新資料 將 pork 的價格改為 35; 將 chicken 的數量改為 30
cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name ='chicken'")
conn.commit()

cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("肉類清單：")
for kind in meat:
    print(kind)
    
#刪除資料 刪除價格為 40 的整筆資料 (前一步驟將pork價格由40改為35，故無資料被刪除)
cursor.execute("DELETE FROM meat WHERE price= 40")
conn.commit()

#查詢資料
cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("肉類清單：")
for kind in meat:
    print(kind)
    
    

#關閉游標和連接
cursor.close()
conn.close()
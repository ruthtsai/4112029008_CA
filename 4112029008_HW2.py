def memory_addressing (page_table , page_size ,logical_address):
    # 計算頁號和偏移量
    page_number , offset = divmod(logical_address , page_size)
    #divmod(除數，被除數)輸出(商，餘)
    
    #查找頁表來獲得相應的框架號
    if page_number in page_table:
        frame_number = page_table[page_number]
        
        #計算物理地址
        physical_address = frame_number * page_size + offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number, address translation failed.")
        
        
        
#定義頁表，其中鍵是頁號，值是框架號
page_table = {}
#print(type(page_table))
while True:
    Add = input("定義頁表請輸入1，完成請輸入2：")
    if Add == "1":
        key = int(input("輸入頁號："))
        value = int(input("輸入框架號："))
        page_table[key] = value
    elif Add == "2":
        break
    

#定義頁大小（例如：4096字節）
page_size = 4096

#定義邏輯地址（例如：7000）
logical_address =int(input("請輸入邏輯地址："))

#調用函數進行地址轉換
memory_addressing(page_table, page_size, logical_address)
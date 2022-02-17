from datetime import datetime
import pymysql
import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host="us-cdbr-east-05.cleardb.net",
                             user="b809ff374c792c",
                             password="bbc8de98",
                             database="heroku_9a97caadd884ab8",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# 打卡：創建時間資料
def daka(EMPNO):
    with connection.cursor() as cursor:
        create_date = datetime.today().strftime('%Y-%m-%d')  # 得到當前日期
        create_time = datetime.today().strftime('%H:%M:%S')  # 得到當前時間
        # 在mysql中，時間資料也是字串，故create_date和create_time還要有一組雙引號
        sql = f"insert into wlog (EMPNO , CREATE_DATE, CREATE_TIME) values ('{EMPNO}', '{create_date}', '{create_time}')"
        cursor.execute(sql)
    connection.commit()
    
    

# 打卡創用範例
# daka(21)  # 自己改數字

# 全選查詢，table --> str
def select_all(table):
    with connection.cursor() as cursor:
        sql = f"select * from {table}"
        cursor.execute(sql)

        # 獲取一筆資料
        result = cursor.fetchone()
        result["CREATE_TIME"] = str(result["CREATE_TIME"])  # 若時間欄位不處理，會得到以秒數表達數值的datetime.timedelta
        print(result,"\n","-"*50)

        # 獲取多筆資料
        result_list = cursor.fetchall()  # 得到list
        for row in result_list:
            row["CREATE_TIME"] = str(row["CREATE_TIME"])  # 若時間欄位不處理，會得到以秒數表達數值的datetime.timedelta
            print(row)
# 查詢叫用範例
# select_all("wlog")
# print("\n","-"*50)

# 目前已知，WLOG新增資料之後，在流水號ID(auto_increment)會呈個位數為4開始且公差為10進行的跡象

# 打卡資料查詢
def select_where(table, EMPNO):
    with connection.cursor() as cursor:
        sql = f"select * from {table} where EMPNO = {EMPNO}"
        cursor.execute(sql)

        # 獲取一筆資料
        # result = cursor.fetchone()
        # result["CREATE_TIME"] = str(result["CREATE_TIME"])  # 若時間欄位不處理，會得到以秒數表達數值的datetime.timedelta
        # print(result,"\n","-"*50)

        # 獲取多筆資料
        result_list = cursor.fetchall()  # 得到list
        for row in result_list:
            row["CREATE_TIME"] = str(row["CREATE_TIME"]) # 若時間欄位不處理，會得到以秒數表達數值的datetime.timedelta
            print(row)
select_where("WLOG", 100)
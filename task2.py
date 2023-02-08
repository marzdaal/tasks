import psycopg2
from config import host, user, password, db_name



try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )

    #Массив со всеми ID которые подходят
    a=[]
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, createdat, statuscode, processing_time, managerid FROM orders")
  
        rows = cursor.fetchall()
        for row in rows:
            if row[2] == 'complete' and ('2022-06' in row[1] or '2022-07' in row[1] or '2022-08' in row[1]):
                if row[4] != 'NULL':
                    a.append(int(row[4]))
        print(set(a))

    #выдает среднее значение по конкретному ID
    m = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, createdat, statuscode, processing_time, managerid FROM orders")
  
        rows = cursor.fetchall()
        for row in rows:
            if row[2] == 'complete' and ('2022-06' in row[1] or '2022-07' in row[1] or '2022-08' in row[1]):
                if row[4] == '49':
                    m.append(int(row[3]))
        print(sum(m)/len(m))

        print("Operation done successfully")  
        connection.close()
    
    

    # Проверка второй таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT code, name, status_group FROM statuses")
  
    #     rows = cursor.fetchall()
    #     for row in rows: 
    #         if row[0] == 'complete':
    #             print("code =", row[0])
    #             print("name =", row[1])
    #             print("status_group =", row[2], "\n")

    #     print("Operation done successfully")  
    #     connection.close() 

except Exception as _ex:
    print("[INFO] Error while ...", _ex)

finally:
    if connection:
        connection.close()
        print('[info] PS close')
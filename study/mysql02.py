import pymysql

data1, data2, data3, data4 = "", "", "", ""
sql = ""

conn = pymysql.connect(host='127.0.0.1', user = 'root', password = '1234', db = 'hanbitdb', charset = 'utf8')
cur = conn.cursor()

while (True):
    data1 = input("사용자 ID ==>")
    if data1 == "":
        break;
    data2 = input("사용자 이름 ==>")
    data3 = input("사용자 이메일 ==>")
    data4 = input("사용자 출생년도==>")
    sql = "INSERT INTO usertable VALUES('"+data1 + "', '"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    
conn.commit()
conn.close()
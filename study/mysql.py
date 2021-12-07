import pymysql

conn = pymysql.connect(host='127.0.0.1', user = 'root', password = '1234', db = 'hanbitdb', charset = 'utf8')

cur = conn.cursor()

try:
    cur.execute("insert into usertable values('HA', 'HAYOSEPH', 'hayswtenv@gmail.com', 1995)")

except:
    conn.rollback()
else :
    conn.commit()
#cur.execute("CREATE TABLE IF NOT EXISTS usertable (id char(4) not null primary key, userName char(15), email char(20), birthYear int)")

#cur.execute("insert into usertable values('HA', 'HAYOSEPH', 'hayswtenv@gmail.com', 1995)")
#conn.commit()




conn.close()
import pymysql as P

Conn=P.connect("localhost", "root", "casper#123", "Project")

Cur=Conn.cursor()

import csv
with open("/Users/aryanagarwal/Desktop/Computer Science/CS Practical/CSProject/CS Project Song Database.csv","r") as n:
    a = csv.reader(n)
    next(a)

    for i in a:
        Command=f'insert into Songs values("{i[0]}","{i[1]}","{i[2]}","{i[3]}",{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]});'
        Cur.execute(Command)
        Conn.commit()

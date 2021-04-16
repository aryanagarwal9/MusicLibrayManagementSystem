import pymysql as P

Conn=P.connect("localhost", "root", "<Enter password>", "<Enter Database Name>")

Cur=Conn.cursor()

import pymysql as P

Conn=P.connect("localhost", "root", "casper#123", "Project")

Cur=Conn.cursor()

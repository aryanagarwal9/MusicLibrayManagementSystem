#This Code is used to transfer the contents of the csv file into a MySQL Table
#test
import pymysql as P

Conn=P.connect("localhost", "root", "<Enter Password>", "<Enter Database Name>")

Cur=Conn.cursor()

Command=f'create table Songs(SNo char(3) primary key, Track_Name varchar(50) not null, Artist_Name varchar(50) not null, Genre varchar(50) not null, BPM int, Energy int, Danceability int, Liveness int, Length int, Popularity int);'
Cur.execute(Command)

import csv
with open("/Users/aryanagarwal/Desktop/Computer Science/CS Practical/CSProject/CS Project Song Database.csv","r") as n:
    a = csv.reader(n)
    next(a)

    for i in a:
        Command=f'insert into Songs values("{i[0]}","{i[1]}","{i[2]}","{i[3]}",{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]});'
        Cur.execute(Command)
        Conn.commit()

from ConnectProject import *



def CreatePlaylist():
    try:
        Command="create table Playlist(SNo int primary key, Track_Name varchar(100) not null, Artist_Name varchar(50) not null, Genre varchar(50) not null, Length int not null);"
        Cur.execute(Command)
        print("Playlist Created")
    except:
        print("Playlist Created!\n")



def Search(TableName, FieldName, UserInput):
    if FieldName=="SNo":
        Command=f"Select * from {TableName} where {FieldName} = {UserInput};"
        Cur.execute(Command)
        Record=Cur.fetchone()
        return Record
    else:
        Command=f"Select * from {TableName} where {FieldName} like '%{UserInput}%';"
        Cur.execute(Command)
        Record=Cur.fetchall()
        return Record



def DisplaySearchForPlaylist(RecordFromSearch):
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index_SNo={}
    Index=1
    for i in RecordFromSearch:
        Index_SNo[Index]=i[0]
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)

    return Index_SNo



def AddToPlaylist(Index_SNo):
    Choice=input("Do you wish to add any song(Y/N)? ").upper()

    if Choice=="N":
        return

    Choice=int(input("Enter Index of Song: "))
    IndexToSNo=Index_SNo.get(Choice)
    if Search('Playlist','SNo',IndexToSNo)==None:
        Record=Search('Songs','SNo', IndexToSNo)
        Command=f'Insert into Playlist values({Record[0]},"{Record[1]}","{Record[2]}","{Record[3]}",{Record[8]});'
        Cur.execute(Command)
        Conn.commit()
        print("Song Added to Playlist")
    else:
        print("Song Already Exists")



def ShowAllSongsInPlaylist():
    Command=f"Select * from Playlist;"
    Cur.execute(Command)
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index_SNo={}
    Index=1
    for i in Record:
        Index_SNo[Index]=i[0]
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)

    return Index_SNo



def DeleteFromPlaylist():
    Index_SNo=ShowAllSongsInPlaylist()
    Choice=int(input("Enter Index Number of Song to be Deleted: "))
    IndexToSNo=Index_SNo.get(Choice)
    if IndexToSNo!=None:
        Command=f"Delete from Playlist where SNo={IndexToSNo};"
        Cur.execute(Command)
        Conn.commit()
        print("Song has been Deleted")
    else:
        print("Invalid Option")



def SortByPopularity():
    Command=f"select * from songs order by Popularity desc limit 5;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)


def SortByEnergy():
    Command=f"select * from songs order by Energy desc limit 5;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)



def SortByBPM():
    Command=f"select * from songs order by BPM desc limit 5;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)



def SortByDanceablilty():
    Command=f"select * from songs order by Danceability desc limit 5;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)



def SearchByTrackName():
    UserInput=input('Enter desired track name :')
    Command=f"select * from songs where Track_Name like '%{UserInput}%' order by Track_Name;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)



def SearchByArtisUserInputame():
    UserInput=input('Enter desired Artist_Name:')
    Command=f"select * from songs where Artist_Name like '%{UserInput}%' order by Artist_Name;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)



def SearchByGenre():
    UserInput=input('Enter desired Genre :')
    Command=f"select * from songs where  Genre like '%{UserInput}%' order by Genre;"
    Cur.execute(Command)
    Conn.commit()
    Record=Cur.fetchall()
    print("="*71)
    TitleRow=f"{'Index':^8}{'Track_Name':^25}{'Artist_Name':^20}{'Genre':^20}"
    print(TitleRow)
    print("="*71)
    Index=1

    for i in Record:
        R= f"{Index:^8}{i[1]:^25}{i[2]:^20}{i[3]:^20}"
        print(R)
        Index+=1
    print("="*71)



def Menu():
    while True:
        print("\n1.Search\n2.Explore\n3.Playlist Options\n4.Exit\n")
        Choice=int(input("Enter Your Choice: "))
        if Choice==1:
            while True:
                print("\n1.By Song Name\n2.By Artist Name\n3.By Genre\n4.Back\n")
                Choice=int(input("Enter Your Choice: "))
                if Choice==1:
                    SearchByTrackName()
                elif Choice==2:
                    SearchByArtisUserInputame()
                elif Choice==3:
                    SearchByGenre()
                elif Choice==4:
                    break
                else:
                    print("\nInvalid Option, Try Again")

        elif Choice==2:
            while True:
                print("\n1.Top Songs\n2.High Energy Songs\n3.Fast Beat Songs\n4.Top Party Songs\n5.Back\n")
                Choice=int(input("Enter Your Choice: "))
                if Choice==1:
                    SortByPopularity()
                elif Choice==2:
                    SortByEnergy()
                elif Choice==3:
                    SortByBPM()
                elif Choice==4:
                    SortByDanceablilty()
                elif Choice==5:
                    break
                else:
                    print("\nInvalid Option, Try Again")


        elif Choice==3:
            while True:
                print("\n1.Show All Songs In Playlist\n2.Search In Playlist\n3.Add Songs to Playlist\n4.Delete Songs from Playlist\n5.Back\n")
                Choice=int(input("Enter Your Choice: "))
                if Choice==1:
                    ShowAllSongsInPlaylist()
                elif Choice==2:
                    UserInput=input("Enter Song Name: ")
                    Record=Search('Playlist','Track_Name',UserInput)
                    DisplaySearchForPlaylist(Record)
                elif Choice==3:
                    UserInput=input("Enter Song: ")
                    Record=Search('Songs', 'Track_Name', UserInput)
                    Index_SNo=DisplaySearchForPlaylist(Record)
                    AddToPlaylist(Index_SNo)
                elif Choice==4:
                    DeleteFromPlaylist()
                elif Choice==5:
                    break
                else:
                    print("\nInvalid Option, Try Again")

        elif Choice==4:
            break

        else:
            print("\nInvalid Option, Try Again")
Menu()

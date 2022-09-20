# cursor object
#  performs operations on a database
#  can begin to execute commmands on the contents of the database using execute() method.
# allows us to process rows insql
# interacts with the mysql server

# import sqlite3
# conn = sqlite3.connect("college.db")
# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS Student")
# cur.execute("CREATE TABLE Students(StudentID INTEGER, StudentName TEXT)")
# conn.commit()
# conn.close()
# print("Table Created")

# def addStudentInfo(StudentID, StudentName):
#     import sqlite3
#     conn = sqlite3.connect("college.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO Students  VALUES (?,?)",(StudentID,StudentName))
#     conn.commit()
#     conn.close()
#     print("Data Inserted")
# addStudentInfo(890, 'Miriam')
# addStudentInfo(891, 'Charles')
# addStudentInfo(892, 'Faith')
# addStudentInfo(893,'Daniel')

def viewstudentinfo():
    import sqlite3
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("SELECT* FROM Students")
    records = cur.fetchall()
    print(records)
    input()
    conn.close()
    print(records)
viewstudentinfo()
c = [i[0] for i in ]

# import sqlite3
# conn = sqlite3.connect("Music.db")
# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS Tracks")
# cur.execute("CREATE TABLE Tracks(Title TEXT, Plays INTEGER)")
# conn.commit()
# conn.close()
# print("Table Created")

# def addTrackinfo(Title, Plays):
#     import sqlite3
#     conn = sqlite3.connect("Music.db")
#     cur =conn.cursor()
#     cur.execute("INSERT INTO Tracks VALUES (?,?)",(Title, Plays))
#     conn.commit()
#     conn.close()
#     print("DATA INSERTED")
# addTrackinfo("Thunderstruck", 20)
# addTrackinfo("Undecided",60)
# addTrackinfo("My Way",15)

# def updateTrack():
#     import sqlite3
#     conn = sqlite3.connect("Music.db")
#     cur = conn.cursor()
#     cur.execute("UPDATE Tracks SET plays = 35 WHERE Title ='Undecided'")
#     cur.execute("UPDATE Tracks SET plays = 20 WHERE Title ='My Way'")
#     conn.commit()
#     conn.close()
#     print("single track Updated!")
# updateTrack()


import sqlite3
from sqlite3.dbapi2 import Connection, Cursor

Connection = sqlite3.connect("movies.db")
Cursor = Connection.cursor

Connection.execute("Create Table Movies (Moviename Text, ParentalGuidance int, MovieCode int, MovieDay Text, MoviePrice int)")
Connection.commit()
print("Table Created")


def addMoviesinfo(Moviesname, ParentalGuidance, MovieCode, MovieDay, MoviePrice):
    import sqlite3
    conn = sqlite3.connect("Movies.db")
    cur =conn.cursor()
    cur.execute("INSERT INTO Movies VALUES (?,?,?,?,?)",(Moviesname, ParentalGuidance, MovieCode, MovieDay, MoviePrice))
    conn.commit()
    conn.close()
    print("DATA INSERTED")
addMoviesinfo("Attack On Titan", 18, 20210, "Saturday", 2500)
addMoviesinfo("Hell hath no fury", 18, 20211, "Friday", 2500)
addMoviesinfo("Die Hard Trying", 18, 20212, "Friday", 3000)
addMoviesinfo("El Dorado", 13, 20213, "Saturday", 3000)
addMoviesinfo("Baby Boss", 15, 20214, "Friday", 2500)
addMoviesinfo("Suicide Squad", 18, 20215, "Saturday", 3000)
addMoviesinfo("Venom 2", 18, 20216, "Friday", 3000)
addMoviesinfo("Sponge bob The Movie", 13, 20217, "Saturday", 25000)
addMoviesinfo("Death Note", 18, 20218, "Friday", 3000)
addMoviesinfo("The Emoji Movie", 18, 20219, "Saturday", 2500)

# import sqlite3
# from sqlite3.dbapi2 import SQLITE_SELECT
# conn = sqlite3.connect("Movies.db")
# cur =conn.cursor()
# for i in range (3):
#     usersname = input ("Enter your name")
#     movieday = input ("Enter your movie date")
#     usersage = input ("Enter users age")
# item =cur.execute("SQLITE_SELECT ParentalGuidance *from movies" )
# for items in item:
#         if usersage < item:
#             status = False
#             print("cannot watch this movie")
#         else:
#             print ("Accepted")
# conn.commit ()
# conn.close()


#     if (items) > (usersage): 
#                  print ('Accepted')
# else: 
#             print ('You are too young to watch this movie')
# c


#     # for entry in addMoviesinfo:
#     #     if usersage < entry in addMoviesinfo [1]:
#     #         print ("Abort Booking. You are not old enough to view this movie")
#     #     else:
#     #         print ("Accepted")






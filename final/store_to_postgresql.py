import psycopg2
from datetime import datetime
global str

data = "5C620DC4F5FC,216.40,0.23,50.0,1.00,60.0,0.10,1"
x = data.split(",")

date = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S")


conn = psycopg2.connect(database="smartpju_v1", user = "postgres", password = "D4n0v4@2020", host = "danova.id", port = "5432")

print ("Opened database successfully")



cur = conn.cursor()

post = """INSERT INTO sensor ("id_device","Tegangan","arus","frequensi","power_factor","daya","energi","status","waktu")VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
data = (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7], date)
cur.execute(post, data)

#
# cur.execute("INSERT INTO belajar (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# cur.execute("INSERT INTO belajar (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# cur.execute("INSERT INTO belajar (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully")

conn.close()

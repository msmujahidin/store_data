import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="D4n0v4@2020",
                                  host="danova.id",
                                  port="5432",
                                  database="smartpju_v1")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from status"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   print (mobile_records[-1])
  #for row in mobile_records:
      # print("Id = ", row[0], )
      # print("Model = ", row[1])
      # print("status  = ", row[0], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

# finally:
#     #closing database connection.
#     if(connection):
#         cursor.close()
#         connection.loop_forever()
#         print("PostgreSQL connection is closed")

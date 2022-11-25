import os
import mysql.connector as database

#username = os.environ.get("kas")
#password = os.environ.get("password")

connection = database.connect(
    user="kas",
    password="password",
    host="localhost",
    database="snmp_collect")

cur = connection.cursor()

def add_data():
    try:
        statement = "INSERT INTO octets (id,name,inoctets,outoctets) VALUES (%s,%s,%s,%s)"
        data = (1,"machine a",100,200)
        cur.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")

add_data()

def get_data(last_name):
    try:
      statement = "SELECT * FROM octets"
      cur.execute(statement)
      print(cursor)
      #for (id,"name","inoctets","outoctets") in cursor:
      #  print(f"Successfully retrieved {first_name}, {last_name}")
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")

"""
try:
    conn = mariadb.connect(
        user="root@localhost",
        password="",
        host="localhost",
        port=3306,
        database="snmp_collect")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

cur.execute("INSERT INTO octets VALUES (1, machine a, 100, 200)")

cur.execute("SELECT * FROM octets")
"""
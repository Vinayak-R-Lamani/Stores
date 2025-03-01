import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root" , 
    password = "Loser$98888",
    database = "stores"
)
cursor  = conn.cursor()

if __name__ == "__main__":
    cursor.execute("show tables")
    tables = [table[0] for table in cursor]
    print(tables)
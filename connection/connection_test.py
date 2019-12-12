from mysql.connector import MySQLConnection, Error

try:
    conn = MySQLConnection(host="localhost",
                           database="mysql",
                           user="root",
                           password='rootroot')
    print(conn)
except Error as e:
    print(e)
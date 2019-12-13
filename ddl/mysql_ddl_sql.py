from mysql.connector import Error, errorcode

from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool

DB_NAME = 'coffee'
TABLES = {'product':(
    """
    create table product (
        code char(4) not null,
        name varchar(20) null,
        primary key(code))
    """
), 'sale':(
    """
    create table sale(
        no int(11) auto_increment,
        code char(4) not null,
        price int(11) not null,
        saleCnt int(11) not null,
        marginRate int(11) not null,
        primary key(no),
        foreign key(code) references product(code))
    """
)}


def create_database():
    try:
        conn = ExplicitlyConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute("create database {} default character set 'utf8'".format(DB_NAME))
        print("create database {}".format(DB_NAME))
    except Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXITST:
            cursor.execute("drop database {}".format(DB_NAME))
            print("drop database {}".format(DB_NAME))
            cursor.execute("create database {} default character set 'utf8'".format(DB_NAME))
            print("create database {}".format(DB_NAME))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def create_table():
    try:
        conn = ExplicitlyConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute("use {}".format(DB_NAME))
        for table_name in TABLES:
            table_description = TABLES[table_name]
            print('table_description', table_description)
            try:
                print("creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
    except Error as err:
        print(err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
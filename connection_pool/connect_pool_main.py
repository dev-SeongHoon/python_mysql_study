import inspect

from connection.connection_study01 import connect, connect_use_config
from connection.python_mysql_dbconfig import read_db_config
from connection_pool.connection_pool_study import DatabaseConnectionPool
from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool, get_implicitly_connection


def connect_pool01():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


def explicitly_connection_pool():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connectioPool = ExplicitlyConnectionPool.get_instance()
    print("ConnectionPool {}".format(connectioPool))
    connection = connectioPool.get_connection()
    print("Connection {}".format(connection))
    connection.close()


def implicitly_connection_pool():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connectioPool = get_implicitly_connection()
    print("ConnectionPool {}".format(connectioPool))
    connection = connectioPool.get_connection()
    print("Connection {}".format(connection))
    connection.close()


if __name__ == "__main__":
     #for i in range(20):
     #  connect_pool01()
     #
    explicitly_connection_pool()
    implicitly_connection_pool()
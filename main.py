from psycopg import connect

from repositories.repository import RepositoryManager

from tools.executing import Executer

# Это точка входа в программу
if __name__ == "__main__":
    connection = connect(dbname="", host="", user="", password="", port="")

    manager = RepositoryManager(connection)

    executer = Executer(manager=manager)
    executer.execute()

    print("Программа завершена")

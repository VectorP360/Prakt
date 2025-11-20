import sys
from pathlib import Path

from psycopg import connect

sys.path.append(str(Path(__file__).parent.parent))

from src.repositories.repository import RepositoryManager
from src.tools.executing import Executer

# Это точка входа в программу
if __name__ == "__main__":
    connection = connect(
        dbname="postgres",
        host="localhost",
        user="postgres",
        password="postgres",
        port="5432",
    )

    manager = RepositoryManager(connection)

    executer = Executer(manager=manager)
    executer.execute()

    print("Программа завершена")

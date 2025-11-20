from src.clients.scada_terminal_client import ScadaTerminalClient
from src.clients.user_terminal_client import UserTerminalClient
from src.repositories.repository import RepositoryManager


class LeaderClient:
    def __init__(self, manager: RepositoryManager):
        self.manager = manager

    def run(self):
        print(
            "У вас на выбор есть следующие клинты в которых можно работать:\n",
            "1: Клиент работы с таблицей пользователей\n",
            "2: Клиент работы с таблицей SCADA схем\n",
            "0: Выход из программы\n",
        )

        client = int(input("Клиент :"))

        match client:
            case 1:
                return UserTerminalClient(manager=self.manager)

            case 2:
                return ScadaTerminalClient(manager=self.manager)

            case 0:
                return

            case _:
                print("Неизвестный клиент!")

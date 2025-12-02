from src.clients.scada_terminal_client import ScadaTerminalClient
from src.clients.user_terminal_client import UserTerminalClient
from src.repositories.repository import RepositoryManager
from src.schemas.user import UserOut
from tools.db_logger import MEGA_LOGGER_40000


class LeaderClient:
    def __init__(self, manager: RepositoryManager, user: UserOut):
        self.manager = manager
        self.logger = MEGA_LOGGER_40000(manager=manager)
        self.user = user

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
                return UserTerminalClient(manager=self.manager, user=self.user)

            case 2:
                return ScadaTerminalClient(manager=self.manager, user=self.user)

            case 0:
                self.logger.log(user=self.user, operation="EXIT")
                return

            case _:
                print("Неизвестный клиент!")

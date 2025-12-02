from src.repositories.repository import RepositoryManager
from src.enums import Command
from src.schemas.user import UserOut
from src.tools.scada_opener import ScadaOpener
from tools.db_logger import MEGA_LOGGER_40000


class WorkerClient:
    def __init__(self, manager: RepositoryManager, user: UserOut):
        self.facility_repository = manager.get_facility_repository()
        self.scada_scheme_repository = manager.get_scada_scheme_repository()
        self.element_repository = manager.get_element_repository()
        self.conditions_repository = manager.get_conditions_repository()
        self.logger = MEGA_LOGGER_40000(manager=manager)
        self.user = user

    def run(self) -> None:
        operation = None

        while operation != 0:
            print(
                "\nУкажите номер операции, которую хотите выполнить\n",
                "1: Просмотреть вашу SCADA схему\n",
                "2: Просмотреть элементы вашей установки\n",
                "3: Просмотреть состояние вашей установки\n",
                "Для выхода из программы введите 0\n",
            )

            operation = int(input("Операция :"))

            match operation:
                case Command.SHOW_SCADA:
                    scada = self.scada_scheme_repository.get_by_user(
                        user_id=self.user.user_id
                    )
                    scada_opener = ScadaOpener()
                    scada_opener.open_in_browser(svg_code=scada.content)
                    self.logger.log(user=self.user, operation="READ")

                case Command.SHOW_ELEMENT:
                    for founded_element in self.element_repository.get_by_user(
                        user_id=self.user.user_id
                    ):
                        print(founded_element)
                        self.logger.log(user=self.user, operation="READ")

                case Command.SHOW_STATUS:
                    print(
                        self.conditions_repository.get_by_user(
                            user_id=self.user.user_id
                        )
                    )
                    self.logger.log(user=self.user, operation="READ")

                case Command.EXIT:
                    self.logger.log(user=self.user, operation="EXIT")
                    return

                case _:
                    print("Выбрана неизвестная операция")
                    return

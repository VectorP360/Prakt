from repository.repository import RepositoryManager
from enums import Command
from enums import Acceptance

from schemas.scada_scheme import ScadaSchemeIn, ScadaSchemeOut
from schemas.user import UserOut

from tools.scada_opener import ScadaOpener



class WorkerClient:
    def __init__(self, manager: RepositoryManager, user: UserOut):
        self.facility_repository = manager.get_facility_repository()
        self.scada_scheme_repository = manager.get_scada_scheme_repository()
        self.element_repository = manager.get_element_repository()
        self.conditions_repository = manager.get_conditions_repository()
        self.user = user

    def run(self) -> None:
        operation = None

        while operation != 0:
            print('\nУкажите номер операции, которую хотите выполнить\n',
                '1: Просмотреть вашу SCADA схему\n',
                '2: Просмотреть элементы вашей установки\n',
                '3: Просмотреть состояние вашей установки\n',
                'Для выхода из программы введите 0\n')

            operation = int(input('Операция :'))

            match operation:

                case Command.SHOW_SCADA:
                    scada = self.scada_scheme_repository.get_by_user(user_id = self.user.user_id)
                    scada_opener = ScadaOpener()
                    scada_opener.open_in_browser(svg_code = scada.content)

                case Command.SHOW_ELEMENT:
                    for founded_element in self.element_repository.get_by_user(user_id = self.user.user_id):
                        print(founded_element)

                case Command.SHOW_STATUS:
                    print(self.conditions_repository.get_by_user(user_id = self.user.user_id))

                case Command.EXIT:
                    return

                case _:
                    print('Выбрана неизвестная операция')
                    return
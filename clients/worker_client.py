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
        self.user = user

    def run(self) -> None:
        operation = None

        while operation != 0:
            print('Укажите номер операции, которую хотите выполнить\n',
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

                case Command.SHOW_ELEMENT:...

                case Command.SHOW_STATUS:...

                case Command.EXIT:
                    return

                case _:
                    print('Выбрана неизвестная операция')
                    return
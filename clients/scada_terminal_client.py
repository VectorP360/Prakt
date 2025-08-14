from typing import Optional
from time import sleep
import webbrowser
import os

from repository.repository import RepositoryManager
from enums import Command

from schemas.posts import PostsIn, PostsOut
from schemas.facility import FacilityIn, FacilityOut
from schemas.scada_scheme import ScadaSchemeIn, ScadaSchemeOut

class ScadaTerminalClient:
    def __init__(self, manager: RepositoryManager):
        self.facility_repository = manager.get_facility_repository()
        self.posts_repository = manager.get_posts_repository()
        self.user_repository = manager.get_user_repository()
        self.scada_scheme_repository = manager.get_scada_scheme_repository()
        self.facility_types_repository = manager.get_facility_types_repository()
        self.workshop_repository = manager.get_workshop_repository()
        self.manager = manager

    def run(self) -> None:
        operation = None

        while operation != 0:
            print('Укажите номер операции, которую хотите выполнить\n',
                '1: Создание новой записи\n',
                '2: Просмотр записи по ID / всех записей\n',
                '3: Редактирование записи\n',
                '4: удаление записи\n',
                '5: просмотреть работника за конкретной установккой\n\n',
                'Для выхода из программы введите 0\n')

            operation = int(input('Операция :'))

            match operation:
                case Command.CREATE_SCADA:
                    self.add_scada()

                case Command.SELECT_SCADA:
                    self.show_scadas()

                case Command.UPDATE_SCADA:
                    self.update_scada()

                case Command.DELETE_SCADA:
                    self.delete_scada()

                case Command.SHOW_SCADA_USER:
                    self.show_scada_user()

                case Command.EXIT:
                    return

                case _:
                    print('Выбрана неизвестная операция')
                    return

    def add_scada(self):
        print('Для создания записи о SCADA схеме укажите все требуемые данные\n')
        scheme_name = input('Название схемы: ')
        
        new_facility = self.select_facility()
        if not new_facility:
            print('Установки под данным номером не обнаружено')
            input('Нажмите Enter что бы продолжить ')
            return
        svg_path = input('Введите расположение файла SCADA схемы: ')

        with open(svg_path, 'r', encoding='utf-8') as file:
            svg_code = file.read()

        new_scada = self.scada_scheme_repository.create(
            scheme_in = ScadaSchemeIn(name = scheme_name, 
                                      facility = new_facility, 
                                      content = svg_code))
        
        my_file = open("TempFile", "w")
        my_file.write(svg_code)
        my_file.close()
        os.rename('TempFile', 'TempFile.svg')
        filepath = os.path.abspath('TempFile.svg')
        sleep(3)
        webbrowser.open(f'File://{filepath}')
        sleep(3)
        os.unlink('TempFile.svg')

        print(new_scada)


    def show_scadas(self):...


    def update_scada(self):...


    def delete_scada(self):...


    def show_scada_user(self):...

    # Вспомогательные функции:

    def select_facility(self) -> Optional[FacilityOut]:
        facilityes = []
        iteration_number = 0 

        print('\nУстановки:')
        for iteration in self.facility_repository.get_all():
            print(f'Установка №{iteration_number} , {iteration}')
            facilityes.append(iteration.facility_id)
            iteration_number += 1

        facility_id = int(input('Какую установку будет представлять схема?: '))

        try:
            return self.facility_repository.get_by_ID(facilityes[facility_id])
        except IndexError:
            return

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
        
        self.open_in_browser(svg_code)

        print(new_scada)


    def show_scadas(self):
        try:
            select_type = int(input('Вы хотите просмотреть одну запись с конкретным ID или сразу все?\n1: C конкретным ID\n2: Все записи\n'))

            match select_type:
                case Command.SHOW_BY_ID:
                    needed_id = input('Введите ID записи которую хотите просмотреть\n')
                    founded_scheme = self.scada_scheme_repository.get_by_ID(needed_id)
                    
                    if founded_scheme:
                        print(founded_scheme)
                        self.open_in_browser(founded_scheme.content)
                    else:
                        print('Записи с указанным ID не найдено')
                
                case Command.SHOW_ALL:
                    for founded_scheme in (self.scada_scheme_repository.get_all()):
                        print(founded_scheme)
                
                case _:
                    print('Выбрана несуществующая операция')
            input('Нажмите Enter что бы продолжить ')
        except KeyboardInterrupt:
            print('Просмотр записи прерван!')
            input('Нажмите Enter что бы продолжить')
            return


    def update_scada(self):
        try:
            print('Scada схемы: ')
            edit_schema = self.select_schema()

            if not edit_schema:
                print('Схемы под данным номером не обнаружено')
                return
                
            name = str(input('Новое название схемы: '))
                
            facility_in = self.select_facility()

            if not facility_in:
                print('Установки под указанным номером не обнаружено')
                return
            
            upd_scheme = self.scada_scheme_repository.update(
                edit_schema.scheme_id, 
                scada_in = ScadaSchemeIn(
                    name = name,
                    facility = facility_in,
                    content = edit_schema.content
                )
                )

            self.open_in_browser(upd_scheme.content)
            print(upd_scheme)
                    
            input('Нажмите Enter что бы продолжить')
        
        except KeyboardInterrupt:
            print('Редактирование записи прервано!')
            input('Нажмите Enter что бы продолжить')
            return


    def delete_scada(self):...


    def show_scada_user(self):...

    # Вспомогательные функции:

    def select_schema(self) -> Optional[ScadaSchemeOut]:
        schemas = []
        iteration_number = 0

        for iteration in self.scada_scheme_repository.get_all():
            print('Номер схемы: ',iteration_number,'\n',iteration)
            schemas.append(iteration.scheme_id)
            iteration_number += 1

        edit_schema = int(input('\nВведите номер схемы, чью запись хотите изменить: '))

        try:
            return self.scada_scheme_repository.get_by_ID(schemas[edit_schema])
        except IndexError:
            return

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

    def open_in_browser(self, svg_code):

        my_file = open("TempFile", "w")
        my_file.write(svg_code)
        my_file.close()

        os.rename('TempFile', 'TempFile.svg')
        filepath = os.path.abspath('TempFile.svg')

        sleep(3)
        webbrowser.open(f'File://{filepath}')
        sleep(3)
        os.unlink('TempFile.svg')
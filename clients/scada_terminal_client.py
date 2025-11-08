from typing import Optional

from repository.repository import RepositoryManager
from enums import Command
from enums import Acceptance

from schemas.facility import FacilityOut
from schemas.scada_scheme import ScadaSchemeIn, ScadaSchemeOut

from tools.scada_opener import ScadaOpener



class ScadaTerminalClient:
    def __init__(self, manager: RepositoryManager):
        self.facility_repository = manager.get_facility_repository()
        self.user_repository = manager.get_user_repository()
        self.scada_scheme_repository = manager.get_scada_scheme_repository()

    def run(self) -> None:
        operation = None

        while operation != 0:
            print('Укажите номер операции, которую хотите выполнить\n',
                '1: Создание новой записи\n',
                '2: Просмотр записи по ID / всех записей\n',
                '3: Редактирование записи\n',
                '4: Удаление записи\n',
                '5: Просмотреть работника за конкретной установккой\n\n',
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
        
        new_facility = self.__select_facility()
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
        
        scada_opener = ScadaOpener()
        scada_opener.open_in_browser(svg_code = svg_code)

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
                        scada_opener = ScadaOpener()
                        scada_opener.open_in_browser(svg_code = founded_scheme.content)
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
            
            # README: А вот эта строка часто повторяется
            input('Нажмите Enter что бы продолжить') 
            
            # Подозрительно часто
            # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠄⠄⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⠋⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⠈⢻⣿⣿⡄⠄⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⣸⣿⡏⠄⠄⠄⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⣿⣿⠁⠄⠄⢰⣿⣿⣯⠁⠄⠄⠄⠄⠄⠄⠄⠈⠙⢿⣷⡄⠄
            # ⠄⠄⣀⣤⣴⣶⣶⣿⡟⠄⠄⠄⢸⣿⣿⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣷⠄
            # ⠄⢰⣿⡟⠋⠉⣹⣿⡇⠄⠄⠄⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠄
            # ⠄⢸⣿⡇⠄⠄⣿⣿⡇⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
            # ⠄⣸⣿⡇⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠄⠄
            # ⠄⣿⣿⠁⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣧⠄⠄
            # ⠄⣿⣿⠄⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⠄⠄
            # ⠄⣿⣿⠄⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⠄⠄
            # ⠄⢿⣿⡆⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⡇⠄⠄
            # ⠄⠸⣿⣧⡀⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⠃⠄⠄
            # ⠄⠄⠛⢿⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄⣰⣿⣿⣷⣶⣶⣶⣶⠶⠄⢠⣿⣿⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⠄⣿⣿⡇⠄⣽⣿⡏⠁⠄⠄⢸⣿⡇⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⠄⣿⣿⡇⠄⢹⣿⡆⠄⠄⠄⣸⣿⠇⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠄⠈⠻⣿⣿⣿⣿⡿⠏⠄⠄⠄⠄
            # ⠄⠄⠄⠄⠄⠄⠄⠈⠛⠻⠿⠿⠿⠿⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            # Копипастишь? 
            # А как насчет https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
            return
        
    def get_scada_by_user(self, user_id) -> ScadaSchemeOut:
        scheme = self.scada_scheme_repository.get_by_user(user_id = user_id)
        scada_opener = ScadaOpener()
        scada_opener.open_in_browser(svg_code = scheme.content)


    def update_scada(self):
        try:
            print('Scada схемы: ')
            edit_schema = self.__select_schema()

            if not edit_schema:
                print('Схемы под данным номером не обнаружено')
                return
                
            name = str(input('Новое название схемы: '))
                
            facility_in = self.__select_facility()

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

            scada_opener = ScadaOpener()
            scada_opener.open_in_browser(svg_code = upd_scheme.content)
            print(upd_scheme)
                    
            input('Нажмите Enter что бы продолжить')
        
        except KeyboardInterrupt:
            print('Редактирование записи прервано!')
            input('Нажмите Enter что бы продолжить')
            return


    def delete_scada(self):

        try:
            schemas_id = []
            print('\nСхемы:')
            
            for iteration in self.scada_scheme_repository.get_all():
                print(iteration)
                schemas_id.append(iteration.scheme_id)
                
            deleted_schema = int(input('Введите ID scada схемы, чью запись хотите удалить: '))

            if deleted_schema in schemas_id:
                acception = input('\nВы уверенны, что хотите удалить эту запись? \nПосле удаления её нельзя будет восстановить (y/n): ')

                if acception == Acceptance.YES: 
                    if self.scada_scheme_repository.delete(deleted_schema):
                        print('Удаление произшло успешно!')
                    else:
                        print('Удаление не состоялось!')
                
                else:
                    print('Удаление отменено')
                    
                input('Нажмите Enter что бы продолжить')
        except KeyboardInterrupt:
            print('Удаление записи прервано!')
            input('Нажмите Enter что бы продолжить')
            return


    def show_scada_user(self):
        selected_schema = self.__select_schema()
        if not selected_schema:
            print('Схемы под указанным номером не обнаружено!')
            input('Нажмите Enter что бы продолжить')
            return
        print(f'Пользователь, который на данный момент работает с этой scada схемой: {self.user_repository.get_by_scada(selected_schema.scheme_id)}')
        input('Нажмите Enter что бы продолжить')


    # Вспомогательные функции:
    # README: Функции такого рода можно сделать приватными (два подчеркивания в начале названия)
    def __select_schema(self) -> Optional[ScadaSchemeOut]:
        schemas = []
        iteration_number = 0

        for iteration in self.scada_scheme_repository.get_all():
            print('Номер схемы: ',iteration_number,'\n',iteration)
            schemas.append(iteration.scheme_id)
            iteration_number += 1

        selected_schema = int(input('\nВведите номер схемы, чью запись хотите изменить: '))

        try:
            return self.scada_scheme_repository.get_by_ID(schemas[selected_schema])
        except IndexError:
            return

    def __select_facility(self) -> Optional[FacilityOut]:
        print('\nУстановки:')
        
        for facility in self.facility_repository.get_all():
            print(f'{facility.name}: {facility.facility_id}')

        facility_id = int(input('Какую установку будет представлять схема?: '))

        try:
            return self.facility_repository.get_by_ID(facility_id)
        except IndexError:
            return

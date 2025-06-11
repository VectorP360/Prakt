from datetime import datetime

from repository.user_repository import UserRepository
from repository.facility_repository import FacilityRepository
from repository.posts_repository import PostsRepository
from schemas.user import UserIn, UserOut

# TODO: коректная обработка даты, возможность пользователя выходить из любого этапа на стартовый
# TODO: Дать пользователю возможность выбирать не id , а порядковый номер в выводимом списке.


# Тут лучше назвать не UserClass, а TerminalClient. 
# Если ты переименуешь Employee в User, то будет конфликт: в программе есть два класса User и UserClass. 
# При таком наименовании становится непонятно, кто какую роль на себя берет. 
# При наименовании TerminalClient программист понимает, что:
# 1) класс является клиентом в клиент-серверной архитектуре
# 2) этот клиент реализует общение с пользователем через терминал

# Пока он реализован только на взаимодействие с записями пользователей в БД. Пока что этого достаточно, 
# но допиши класс так, чтобы он мог в будущем взять на себя чуть больше возможностей. 
# Например, позволил бы пользователю управлять списком установок, типов, и так далее.  


class TerminalClient:
    def __init__(self, 
                 user_repository: UserRepository, 
                 posts_repository: PostsRepository, 
                 facility_repository: FacilityRepository):
        
        self.user_repository = user_repository
        self.posts_repository = posts_repository
        self.facility_repository = facility_repository


    def run(self) -> None:
        operation = None

        while operation != 0:
            print('Укажите номер операции, которую хотите выполнить\n',
                  '1: Создание новой записи\n',
                  '2: Просмотр записи по ID / всех записей\n',
                  '3: Редактирование записи\n',
                  '4: удаление записи\n\n',
                  'Для выхода из приложения введие 0\n')

            operation = int(input('Операция :'))

            if operation == 1:
                self.add_user()

            if operation == 2:
                self.show_users()

            if operation == 3:
                self.update_user()

            if operation == 4:
                self.delete_user()


    # Не бойся давать переменным более осмысленные названия
    def add_user(self):
        
        print('Для создания записи о сотруднике укажите все перечисленные данные:')
        surname = str(input('Фамилия: '))
        name = str(input('Имя: '))
        fathersname = str(input('Отчество: '))

        print('\nУстановки:')
        
        # TODO: Дополнить класс Facility таким образом, 
        # чтобы при передаче объекта класса Facility в print печатались все данный в таком формате, как указано ниже.
        # Нужно использовать dunder метод
        
        for iteration in self.facility_repository.get_all():
            print(f'''ID: {iteration.facility_id}, Наименование: {iteration.name}, {iteration.type.facility_type_name}, {iteration.workshop.name}, {iteration.scada_scheme.scheme_name}''')
                
        facility = int(input('На какой установке (ID установки) будет работать сотрудник: '))

        print('\nДолжности:')
        
        for iteration in self.posts_repository.get_all():
            print(f'''ID: {iteration.post_ID}, Наименование: {iteration.post_name}''')

        post = int(input('Должность сотрудника (ID должности): '))

        new_hire = int(input('\nЭто новый сотрудник, или старый, которого ещё нет в базе данных?\n1: Новый сотрудник\n2: Старый сотрудник\n'))
        
        if new_hire == 1:
            hire_date = datetime.today()
        elif new_hire == 2:
            hire_date = (input('Дата найма сотрудника (год-месяц-число): '))

        login = str(input('Логин сотрудника: '))
        password = str(input('Личный пароль сотруднка: '))

        new_facility = self.facility_repository.get_by_ID(facility)
        new_post = self.posts_repository.get_by_ID(post)

        # TIP: На экран не помещается строка XD
        # Старайся компоновать код так, чтобы не приходилось его переметывать вбок.
        # В идеале код должен пролистываться только вверх или вниз.
        new_user = self.user_repository.create(
            new_user = UserIn(surname, 
                                      name, 
                                      fathersname, 
                                      facility = new_facility, 
                                      post = new_post, 
                                      hire_date = hire_date, 
                                      login = login, 
                                      password = password))

        # TODO: Дополнить класс User (который в новом create_database.sql назван User) таким образом, 
        # чтобы при передаче объекта класса User в print печатались все данный в таком формате, как указано ниже.
        print(f'''ID {new_user.user_id}, ФИО: {new_user.surname} {new_user.name} {new_user.fathersname}, установка: {new_user.facility.name}, должность: {new_user.post.post_name}, Дата найма: {new_user.hire_date}, Логин {new_user.login}''')
            
        input('Нажмите Enter что бы продолжить ')


    def show_users(self):
        # TODO: Описать возможные варианты ответа на данный вопрос как класс, который наследуется от класса IntEnum 
        # (почитай примеры использования).
        # С использованием данного подхода опиши методы, которые будут инкапсулировать логику, описанную после if и elif. 
        # Аналогично в других частях кода
        select_type = input('Вы хотите просмотреть одну запись с конкретным ID или сразу все?\n1: C конкретным ID\n2: Все записи\n')

        if select_type == '1':
            needed_id = input('Введите ID записи которую хотите просмотреть\n')
            founded_user = self.user_repository.get_by_ID(needed_id)
            
            if founded_user:
                print(f'''ID {founded_user.user_id}, ФИО: {founded_user.surname} {founded_user.name} {founded_user.fathersname}, Установка: {founded_user.facility.name}, Должность: {founded_user.post.post_name}, Дата найма {founded_user.hire_date}, Логин {founded_user.login}''')
            else:
                print('Записи с указанным ID не найдено')
            
        elif select_type == '2':
            for founded_user in (self.user_repository.get_all()):
                print(f'''ID {founded_user.user_id}, ФИО: {founded_user.surname} {founded_user.name} {founded_user.fathersname}, Установка: {founded_user.facility.name}, Должность: {founded_user.post.post_name}, Дата найма {founded_user.hire_date}, Логин {founded_user.login}''')
            
        input('Нажмите Enter что бы продолжить ')


    def update_user(self):

        for iteration in self.user_repository.get_all():
            print(f'''ID: {iteration.user_id}, ФИО: {iteration.surname} {iteration.name} {iteration.fathersname}, должность: {iteration.post.post_name}''')
        
        edit_user = int(input('Введите ID сотрудника, чью запись хотите изменить: '))
        
        if self.user_repository.get_by_ID(edit_user):
            
            surname = str(input('Новая фамилия: '))
            name = str(input('Новое имя: '))
            fathersname = str(input('Новое отчество: '))

            print('\nУстановки:')
            
            for iteration in self.facility_repository.get_all():
                print(f'''ID: {iteration.facility_id}, Наименование: {iteration.name}, {iteration.type.facility_type_name}, {iteration.workshop.name}, {iteration.scada_scheme.scheme_name}''')
                    
            facility_id = int(input('На какой установке (ID установки) будет работать сотрудник: '))

            if self.facility_repository.get_by_ID(facility_id):

                print('\nДолжности:')
                for iteration in self.posts_repository.get_all():
                    print(f'''ID: {iteration.post_ID}, Наименование: {iteration.post_name}''')

                post = int(input('Должность сотрудника (ID должности): '))

                if self.posts_repository.get_by_ID(post):
                    
                    new_hire = int(input('\nЭто новый сотрудник, или старый, которого ещё нет в базе данных?\n1: Новый сотрудник\n2: Старый сотрудник\n'))
                    if new_hire == 1:
                        hire_date = datetime.today()
                    elif new_hire == 2:
                        hire_date = int(input('Дата найма сотрудника (год-месяц-число): '))
                    login = str(input('Новый логин сотрудника: '))
                    password = str(input('Новый личный пароль сотруднка: '))

                    facility_in = self.facility_repository.get_by_ID(facility_id)
                    post_in = self.posts_repository.get_by_ID(post)

                    upd_user = self.user_repository.update(edit_user, new_user = UserIn(surname, name, fathersname, facility_in, post_in, hire_date, login, password))

                    print(f'''ID {upd_user.user_id}, ФИО: {upd_user.surname} {upd_user.name} {upd_user.fathersname}, установка: {upd_user.facility.name}, должность: {upd_user.post.post_name}, Дата найма: {upd_user.hire_date}, Логин {upd_user.login}''')
                else:
                    print('Должности с указанным ID не обнаружено')
            else:
                print('Установки с указанным ID не обнаружено')
        else:
            print('Сотрудника с данным ID не обнаружено')
        input('Нажмите Enter что бы продолжить')


    def delete_user(self):
                
        print('\nСотрудники:')
        
        # Подсказка: надо описать dunder метод
        for iteration in self.user_repository.get_all():
            print(f'''ID: {iteration.user_id}, ФИО: {iteration.surname} {iteration.name} {iteration.fathersname}, должность: {iteration.post.post_name}''')
            
        deleted_user = input('Введите ID сотрудника, чью запись хотите удалить: ')
        acception = input('\nВы уверенны, что хотите удалить эту запись? \nПосле удаления её нельзя будет восстановить (y/n): ')

        if acception == 'y':
                        
            if self.user_repository.delete(deleted_user):
                print('Удаление произшло успешно!')
            else:
                print('Удаление не состоялось!')
            
            input('Нажмите Enter что бы продолжить')

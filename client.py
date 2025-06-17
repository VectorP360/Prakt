from datetime import datetime

from repository.repository import RepositoryManager
from schemas.user import UserIn, UserOut
from update_id_to_list import list_for_users, list_for_facilityes, list_for_posts
from password_generator import password_generator

# TODO: коректная обработка даты [X] , возможность пользователя выходить из любого этапа на стартовый []
# TODO: Дать пользователю возможность выбирать не id , а порядковый номер в выводимом списке. [X]


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
    def __init__(self, manager: RepositoryManager): 
        self.facility_repository = manager.get_facility_repository()
        self.posts_repository = manager.get_posts_repository()
        self.user_repository = manager.get_user_repository()
        self.scada_scheme_repository = manager.get_scada_scheme_repository()
        self.facility_types_repository = manager.get_facility_types_repository()
        self.workshop_repository = manager.get_workshop_repository()

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
        
        try:
            print('Для создания записи о сотруднике укажите все перечисленные данные:')
            surname = str(input('Фамилия: '))
            name = str(input('Имя: '))
            fathersname = str(input('Отчество: '))
            
            # TODO: Дополнить класс Facility таким образом, 
            # чтобы при передаче объекта класса Facility в print печатались все данный в таком формате, как указано ниже. [X]
            # Нужно использовать dunder метод
            
            new_facility = list_for_facilityes(self.facility_repository)
            if not new_facility:
                print('Установки под данным номером не обнаружено')
                input('Нажмите Enter что бы продолжить ')
                return

            new_post = list_for_posts(self.posts_repository)
            if not new_post:
                print('Должности под данным номером не обнаружено')
                input('Нажмите Enter что бы продолжить ')
                return

            new_hire = int(input('\nЭто новый сотрудник, или старый, которого ещё нет в базе данных?\n1: Новый сотрудник\n2: Старый сотрудник\n'))
            
            if new_hire == 1:
                hire_date = datetime.today()
            elif new_hire == 2:
                hire_date = datetime.strptime(str(input('Дата найма сотрудника (год-месяц-число): ')), '%y-%m-%d')

            login = str(input('Логин сотрудника: '))
        except KeyboardInterrupt:
            print('\nВыполнение программы прервано!')
            input('Нажмите Enter что бы продолжить')
            return

        if new_post.post_ID == 1 or new_post.post_ID == 2:
            password_length = 12
        else:
            password_length = 8

        password = password_generator(password_length)

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

        # TODO: Дополнить класс User таким образом, 
        # чтобы при передаче объекта класса User в print печатались все данный в таком формате, как указано ниже. [X]
        print(new_user)
            
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
                print(founded_user)
            else:
                print('Записи с указанным ID не найдено')
            
        elif select_type == '2':
            for founded_user in (self.user_repository.get_all()):
                print(founded_user)
            
        input('Нажмите Enter что бы продолжить ')


    def update_user(self):
        
        try:
            print('Сотрудники: ')
            edit_user = list_for_users(self.user_repository)

            if not edit_user:
                print('Сотрудника под данным номером не обнаружено')
                return
                
            surname = str(input('Новая фамилия: '))
            name = str(input('Новое имя: '))
            fathersname = str(input('Новое отчество: '))
                
            facility_in = list_for_facilityes(self.facility_repository)

            if not facility_in:
                print('Установки под указанным номером не обнаружено')
                return

            post_in = list_for_posts(self.posts_repository)

            if not post_in:
                print('Должности под указанным номером не обнаружено')
                return

            login = str(input('Новый логин сотрудника: '))
            password = str(input('Новый личный пароль сотруднка: '))

            upd_user = self.user_repository.update(
                edit_user.user_id, 
                new_user = UserIn(
                    surname, 
                    name, 
                    fathersname, 
                    facility_in, 
                    post_in, 
                    edit_user.hire_date, 
                    login, 
                    password)
                )

            print(upd_user)
                    
            input('Нажмите Enter что бы продолжить')
        
        except KeyboardInterrupt:
            print('Редактирование записи прервано!')
            input('Нажмите Enter что бы продолжить')
            return


    def delete_user(self):
        
        users_id = []
        print('\nСотрудники:')
        
        for iteration in self.user_repository.get_all():
            print(f'''ID: {iteration.user_id}, ФИО: {iteration.surname} {iteration.name} {iteration.fathersname}, должность: {iteration.post.name}''')
            users_id.append(iteration.user_id)
            
        deleted_user = input('Введите ID сотрудника, чью запись хотите удалить: ')

        if deleted_user not in users_id:
            acception = input('\nВы уверенны, что хотите удалить эту запись? \nПосле удаления её нельзя будет восстановить (y/n): ')

            if acception == 'y':
                            
                if self.user_repository.delete(deleted_user):
                    print('Удаление произшло успешно!')
                else:
                    print('Удаление не состоялось!')
                
                input('Нажмите Enter что бы продолжить')

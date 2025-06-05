# Соблюдай следующий порядок импортов:
# Сначала идут системные библиотеки, которые реализованы внутри самого Python
# Затем идут библиотеки установелнные через pip
# Потом те модули, которые реализованы программистами в рамках текущего проекта

# Лучше импоритровать элементы модулей по мере их нужности, как покащано ниже 
# Читаемость будет лучше и ты как программист будешь уверен, 
# что все импортированное отсюда будет так или иначе использвано

# Классы из данного модуля являются вспомогательными для программиста и обязательными для анализаторов кода
from typing import List, Optional

from psycopg import Connection
from psycopg.errors import UniqueViolation

from table_classes.workshop import Workshop

class WorkshopRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, workshop_id: int, workshop_name: str)->Optional[Workshop]:
        cursor = self.__connection.cursor()
        try:
            # Никогда (!!!) не используй в SQL запросах f-строки и никогда (!!!) не склеивай строки, 
            # так как через них можно протащить вредоносные запросы (DROP DATABASE например). 
            # Почитай про SQL-инъекции и чем они опасны
            
            # Для метода execute в качестве второго аргумента можно передавать кортеж параметров.
            # Каждому параметру соответствует свой %s в SQL запросе.
            # Первый %s - это workshop_id в коде
            # Второй %s - это workshop_name
            
            cursor.execute(
            '''
            INSERT INTO workshop (workshop_id, workshop_name) VALUES (%s, %s);
            ''', (workshop_id, workshop_name)
            )
            self.__connection.commit()
        except UniqueViolation:
            
            print('Запись с данным ID уже существует')
            self.__connection.commit()
            # Если метод может что-то не вернуть в силу каких-то причин, 
            # то указывай возвращаемый тип как опциональный (Optional)
            
            return None
        
        return Workshop(workshop_id, workshop_name)
        

    # Лучше всегда указывать типы для передаваемых переменных 
    # и для возвращаемых функций.
    def get_by_ID(self, workshop_id: str) -> Optional[Workshop]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT * FROM workshop WHERE workshop_ID = %s''', (workshop_id,))

        fetched_row = cursor.fetchone()
        
        # Проверки на пустоту типа (является объект None или нет) 
        # можно описать сокращенно, как ниже
        
        if fetched_row:
            return Workshop(fetched_row[0], fetched_row[1])
        else:
            return None
    
    
    def get_all(self) -> List[Workshop]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT * FROM workshop ORDER BY workshop_ID;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = Workshop(record[0], record[1])
            result.append((new_obj.workshop_id,new_obj.name))  #Таким образом будет возращаться не список из объектов
                                                               #а из кортежей, содержащих атрибуты этих объектов 
        return result


    # Как программист, который будет пользоваться данным кодом, поймет, 
    # произошло измененеи данных или нет? Метод поитогу ничего не возвращает
    def update(self, workshop_id: str, new_name: str) -> None:
        cursor = self.__connection.cursor()

        cursor.execute('''
        UPDATE workshop SET workshop_name = %s WHERE workshop_id = %s
        ''', (new_name, workshop_id,)
        )
        
        self.__connection.commit()

        return None

    # Как программист, который будет использоваться данный код, поймет, 
    # что удаление произошло успешно?
    # Потому что тут тоже поитоге метод ничего не возвращает
    def delete(self, workshop_id: int) -> None:
        cursor = self.__connection.cursor()

        try:
            cursor.execute('''DELETE FROM workshop WHERE workshop_ID = %s''', (workshop_id,))
            self.__connection.commit()
        
        except UniqueViolation: 
            print('Записи с данным ID не было обнаружено')

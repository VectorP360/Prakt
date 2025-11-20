from typing import List, Optional

from psycopg import Connection
from psycopg.rows import kwargs_row # Это самый удобный генератор строк на мой взгляд

from schemas.facility import FacilityOut, FacilityIn, FacilityTypeOut, WorkshopOut


class FacilityRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, new_facility: FacilityIn)-> Optional[FacilityOut]:
        # README: Пару недель назад я обнаружил в Psycopg фичу, которая облегчает возврат строк из БД
        
        # Почитать можно вот тут
        # https://www.psycopg.org/psycopg3/docs/api/rows.html

        # Показываю, что нужно делать:
        
        # === ПОКАЗЫВАЮ ===
        # 1) Ты определяешь функцию, которая принимает на вход строку прямо из БД. 
        # def object_from_row(**row) -> Object:
        #   return Object(field1=row['field1'], field2=row['field2'])  

        # **row - это краткое описаение json-like словаря, где ключи - строки, а значения могут быть любого типа
        
        # 2) При создании курсора (объекта для работы с БД) 
        # в качестве параметра row_factory передаешь свою функцию, 
        # но обернутую в kwargs_row (я оставил импорт выше)
        
        # cursor = self.__connection.cursor(row_factory=kwargs_row(object_from_row))
        # === ПЕРЕСТАЛ ПОКАЗЫВАТЬ ===
        
        # В Python функции тоже являются объектами, как переменные типа int, str, float. 
        # Функции - это объекты типа Callable.
        # То есть, при создании курсора в строке выше ты вызываешь метод объекта подключения (Connection), 
        # передевая в качестве аргумента row_factory объект kwargs_row (которая является объектом типа Callable), 
        # в который в СВОЮ очередь передаешь объект object_from_row (тоже объект типа Callable)

        # Если ничего не понял, то это нормально
        # ⣿⣿⣿⣿⣿⢿⠿⠿⠿⠛⠛⠛⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿
        # ⣿⣿⠟⠋⣁⠄⠄⣀⣤⣤⣤⣀⣉⣁⡀⠒⠄⠉⠛⣿⣿⣿⣿⣿
        # ⡏⢡⣴⠟⠁⠐⠉⠄⣤⣄⠉⣿⠟⢃⡄⠄⠄⢠⡀⠈⠻⣿⣿⣿
        # ⠄⢸⣤⣤⣀⠑⠒⠚⠛⣁⣤⣿⣦⣄⡉⠛⠛⠛⠉⣠⣄⠙⣿⣿
        # ⠄⣾⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠚⣿
        # ⠄⢻⣿⣿⣷⣄⣉⠙⠛⠛⠛⠛⠛⠛⠋⣉⣉⣀⣤⠤⠄⣸⡀⢻
        # ⣇⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣶⣿⣇⠘
        # ⣿⣧⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⣿⡿⠄
        # ⣿⣿⣷⡀⠹⣿⣿⣿⣿⣿⣿⡋⠙⢻⣿⣿⣿⠟⢀⣾⣿⣿⠃⣸
        # ⣿⣿⣿⣿⣦⠈⠻⣿⣿⣿⣿⣿⣷⣤⣀⣀⣠⣤⣿⣿⠟⢁⣼⣿
        # ⣿⣿⣿⣿⣿⣿⣶⣤⣈⠙⠛⠛⠿⠿⠿⠿⠿⠛⠛⣡⣴⣿⣿⣿
        # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿
        # Погугли
             
        cursor = self.__connection.cursor(row_factory=kwargs_row())

        def from_row(**row):
            pass


        cursor.execute(
        '''
        INSERT INTO facility (name, facility_type_id, workshop_id) VALUES (%s,%s,%s)
        RETURNING facility_id, name,facility_type_id, workshop_id
        ''', (new_facility.name, new_facility.type.facility_type_id, new_facility.workshop.workshop_id,)
        )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                facility_id=fetched_row[0],
                name=fetched_row[1],
                type= new_facility.type, 
                workshop= new_facility.workshop
                )
        return None
        

    def get_by_ID(self, facility_id: int) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                       SELECT facility_id, facility.name, type_id, facility_type.name, workshop_id, workshop.name
                       FROM facility 
                        JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                        JOIN workshop USING (workshop_id)
                       WHERE facility_id = %s
                       ''', (facility_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                fetched_row[0],
                fetched_row[1], 
                type = FacilityTypeOut(
                    facility_type_id=fetched_row[2],
                    name = fetched_row[3]
                ), 
                workshop = WorkshopOut(
                    workshop_id= fetched_row[4],
                    name= fetched_row[5]
                )
                )
        else:
            return None
    

    def get_by_name(self, name: str) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                       SELECT facility_id, facility.name, type_id, facility_type.name, workshop_id, workshop.name
                       FROM facility 
                        JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                        JOIN workshop USING (workshop_id)
                       WHERE facility.name = %s
                       ''', (name,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                fetched_row[0],
                fetched_row[1], 
                type = FacilityTypeOut(
                    facility_type_id=fetched_row[2],
                    name = fetched_row[3]
                ), 
                workshop = WorkshopOut(
                    workshop_id= fetched_row[4],
                    name= fetched_row[5]
                )
                )
        else:
            return None

    
    def get_all(self) -> List[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                        SELECT facility_id, facility.name, facility_type_id, facility_type.name, workshop_id,
                            workshop.name
                        FROM facility
                        JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                        JOIN workshop USING (workshop_id)
                        ORDER BY facility_id;
                       ''')
        
        result = []        
        for record in cursor.fetchall():
            type = FacilityTypeOut(record[2],record[3])
            workshop = WorkshopOut(record[4],record[5])
            new_obj = FacilityOut(record[0], record[1],type = type, workshop = workshop)
            result.append(new_obj)  
        return result


    def update(self, facility_id: int, new_facility: FacilityIn) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE facility SET name = %s, facility_type_id = %s, workshop_id = %s
        WHERE facility_id = %s

        RETURNING facility_id, facility_name
        ''', 
        (new_facility.name, new_facility.type.facility_type_id, new_facility.workshop.workshop_id, facility_id,)
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            type = new_facility.type
            workshop = new_facility.workshop
            return FacilityOut(
                fetched_row[0], 
                fetched_row[1], 
                type, 
                workshop)
        else:
            return None


    def delete(self, facility_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM facility WHERE facility_id = %s''', (facility_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
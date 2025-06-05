import psycopg
import table_classes.workshop as workshop

class WorkshopRepository:
    def __init__(self, connection: psycopg.Connection):
        self.__conn = connection

    def create(self, workshop_id: int, workshop_name: str):
        cursor = self.__conn.cursor()
        try:
            cursor.execute(f'''
            INSERT INTO workshop (workshop_id, workshop_name) VALUES ({workshop_id}, '{workshop_name}');
            ''')
            self.__conn.commit()
        except psycopg.errors.UniqueViolation: #Ошибка при создании записи (Повторение ключа)
            print('Запись с данным ID уже существует')

        return workshop.Workshop(workshop_id, workshop_name)


    def get_by_ID(self, workshop_id):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM workshop WHERE workshop_ID = {workshop_id};
        ''')

        result = cursor.fetchone()
        if result != None:
            new_obj = workshop.Workshop(result[0],result[1])
            return new_obj.__dict__
        else:
            return 'Записи с данным ID не обнаружено'

    
    def get_all(self):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM workshop ORDER BY workshop_ID;
        ''')
        
        query = cursor.fetchall()
        result = []
                
        for iteration in query:
            new_obj = workshop.Workshop(iteration[0],iteration[1])
            result.append(new_obj.__dict__)

        return result

    def update(self, workshop_id, new_name):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        UPDATE workshop SET workshop_name = '{new_name}' WHERE workshop_id = {workshop_id}
        ''')
        self.__conn.commit()

    def delete(self, workshop_id: int):
        cursor = self.__conn.cursor()

        try:
            cursor.execute(f'''DELETE FROM workshop WHERE workshop_ID = {workshop_id} ''')
            self.__conn.commit()
        except psycopg.errors.UniqueViolation: 
            print('Записи с данным ID не было обнаружено')
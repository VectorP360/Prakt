import psycopg
import workshop

class WorkshopRepository:
    def __init__(self, connection: psycopg.Connection):
        self.__conn = connection

    def create(self, workshop_id: int, workshop_name: str):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        INSERT INTO workshop (workshop_id, workshop_name) VALUES ({workshop_id}, '{workshop_name}');
        ''')

        self.__conn.commit()
        return workshop.Workshop(workshop_id, workshop_name)


    def get_by_ID(self, workshop_id):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM workshop WHERE workshop_id = {workshop_id};
        ''')
        
        return cursor.fetchall()
    
    def get_all(self):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM workshop;
        ''')
        
        return cursor.fetchall()

    def update(self, workshop_id, new_name):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        UPDATE workshop SET workshop_name = '{new_name}' WHERE workshop_id = {workshop_id}
        ''')
        self.__conn.commit()

    def delete(self, workshop_id: int):
        cursor = self.__conn.cursor()

        cursor.execute(f'''DELETE FROM workshop WHERE workshop_ID = {workshop_id} ''')
        self.__conn.commit()
import psycopg
import table_classes.facility_types as facility_types

class FacilityTypesRepository:
    def __init__(self, connection: psycopg.Connection):
        self.__conn = connection

    def create(self, type_id: int, type_name: str):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        INSERT INTO facility_types (type_id, type_name) VALUES ({type_id}, '{type_name}');
        ''')

        self.__conn.commit()
        return facility_types.FacilityTypes(type_id, type_name)


    def get_by_ID(self, type_id):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM facility_types WHERE type_id = {type_id};
        ''')
        
        return cursor.fetchall()
    
    def get_all(self):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM facility_types;
        ''')
        
        return cursor.fetchall()

    def update(self, type_id, new_name):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        UPDATE facility_types SET type_name = '{new_name}' WHERE type_id = {type_id}
        ''')
        self.__conn.commit()

    def delete(self, type_id: int):
        cursor = self.__conn.cursor()

        cursor.execute(f'''DELETE FROM facility_types WHERE type_ID = {type_id} ''')
        self.__conn.commit()
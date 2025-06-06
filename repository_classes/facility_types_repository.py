from typing import List, Optional

from psycopg import Connection

from table_classes.facility_types import FacilityTypesOut, FacilityTypesIn

class FacilityTypesRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, type_name: str)-> FacilityTypesIn:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO facility_types (type_name) VALUES (%s)
        ON CONFLICT (type_id) DO NOTHING
        ''', (type_name,)
        )
        self.__connection.commit()
        
        return FacilityTypesIn(type_name)
        

    def get_by_ID(self, type_id: str) -> Optional[FacilityTypesOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT type_id, type_name FROM facility_types WHERE type_ID = %s''', (type_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityTypesOut(fetched_row[0], fetched_row[1])
        else:
            return None
    
    
    def get_all(self) -> List[FacilityTypesOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT type_id, type_name FROM facility_types ORDER BY type_ID;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = FacilityTypesOut(record[0], record[1])
            result.append(new_obj)  
        return result


    def update(self, type_id: str, new_name: str) -> Optional[FacilityTypesOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE facility_types SET type_name = %s WHERE type_id = %s
        RETURNING type_id, type_name;''', (new_name, type_id,)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return FacilityTypesOut(fetched_row[0], fetched_row[1])
        else:
            return None


    def delete(self, type_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM facility_types WHERE type_ID = %s''', (type_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
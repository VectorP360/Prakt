from typing import List, Optional

from psycopg import Connection

from schemas.facility_type import FacilityTypeOut


class FacilityTypeRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, name: str)-> Optional[FacilityTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO facility_type (name) VALUES (%s)
        ON CONFLICT (facility_type_id) DO NOTHING
        RETURNING facility_type_id, name
        ''', (name,)
        )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()
        if fetched_row:
            return FacilityTypeOut(fetched_row[0],fetched_row[1])
        return None
        

    def get_by_ID(self, type_id: str) -> Optional[FacilityTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT facility_type_id, name FROM facility_type WHERE facility_type_id = %s''', (type_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityTypeOut(fetched_row[0], fetched_row[1])
        else:
            return None
    
    
    def get_all(self) -> List[FacilityTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT facility_type_id, name FROM facility_type ORDER BY facility_type_id;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = FacilityTypeOut(record[0], record[1])
            result.append(new_obj)  
        return result


    def update(self, type_id: str, new_name: str) -> Optional[FacilityTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE facility_type SET name = %s WHERE facility_type_id = %s
        RETURNING facility_type_id, name;''', (new_name, type_id,)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return FacilityTypeOut(fetched_row[0], fetched_row[1])
        else:
            return None


    def delete(self, type_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM facility_type WHERE facility_type_id = %s''', (type_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)

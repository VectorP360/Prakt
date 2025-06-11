from typing import List, Optional

from psycopg import Connection

from schemas.workshop import WorkshopOut, WorkshopIn

class WorkshopRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, name: str)-> WorkshopIn:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO workshop (name) VALUES (%s)
        ON CONFLICT (workshop_id) DO NOTHING
        ''', (name,)
        )
        self.__connection.commit()
        
        return WorkshopIn(name)
        

    def get_by_ID(self, workshop_id: str) -> Optional[WorkshopOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT workshop_id, name FROM workshop WHERE workshop_ID = %s''', (workshop_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return WorkshopOut(fetched_row[0], fetched_row[1])
        else:
            return None
    
    
    def get_all(self) -> List[WorkshopOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT workshop_id, name FROM workshop ORDER BY workshop_ID;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = WorkshopOut(record[0], record[1])
            result.append(new_obj)  
        return result


    def update(self, workshop_id: str, new_name: str) -> Optional[WorkshopOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE workshop SET name = %s WHERE workshop_id = %s
        RETURNING workshop_id, name;''', (new_name, workshop_id,)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return WorkshopOut(fetched_row[0], fetched_row[1])
        else:
            return None


    def delete(self, workshop_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM workshop WHERE workshop_ID = %s''', (workshop_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
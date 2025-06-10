from typing import List, Optional

from psycopg import Connection

from schemas.scada_scheme import ScadaSchemeOut, ScadaSchemeIn

class ScadaSchemeRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, scheme_name: str)-> ScadaSchemeIn:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO scada_scheme (scheme_name) VALUES (%s)
        ON CONFLICT (scheme_id) DO NOTHING
        ''', (scheme_name,)
        )
        self.__connection.commit()
        
        return ScadaSchemeIn(scheme_name)
        

    def get_by_ID(self, scheme_id: str) -> Optional[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT scheme_id, scheme_name FROM scada_scheme WHERE scheme_ID = %s''', (scheme_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return ScadaSchemeOut(fetched_row[0], fetched_row[1])
        else:
            return None
    
    
    def get_all(self) -> List[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT scheme_id, scheme_name FROM scada_scheme ORDER BY scheme_ID;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = ScadaSchemeOut(record[0], record[1])
            result.append(new_obj)  
        return result


    def update(self, scheme_id: str, new_name: str) -> Optional[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE scada_scheme SET scheme_name = %s WHERE scheme_id = %s
        RETURNING scheme_id, scheme_name;''', (new_name, scheme_id,)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return ScadaSchemeOut(fetched_row[0], fetched_row[1])
        else:
            return None


    def delete(self, scheme_id: int) -> Optional[ScadaSchemeOut]:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM scada_scheme WHERE scheme_ID = %s''', (scheme_id,))
        self.__connection.commit()
        cursor.execute('''SELECT scheme_id FROM scada_scheme WHERE scheme_id = %s''',(scheme_id,))
        fetchet_row = cursor.fetchone()

        if fetchet_row:
            return ScadaSchemeOut(fetchet_row[0], fetchet_row[1])
        else:
            return None
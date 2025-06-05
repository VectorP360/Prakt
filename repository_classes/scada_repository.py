import psycopg
import table_classes.scada_scheme as scada_scheme

class SCADARepository:
    def __init__(self, connection: psycopg.Connection):
        self.__conn = connection

    def create(self, scheme_id: int, scheme_name: str):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        INSERT INTO scada_scheme (scheme_id, scheme_name) VALUES ({scheme_id}, '{scheme_name}');
        ''')

        self.__conn.commit()
        return scada_scheme.SCADA_scheme(scheme_id, scheme_name)


    def get_by_ID(self, scheme_id):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM scada_scheme WHERE scheme_id = {scheme_id};
        ''')
        
        return cursor.fetchall()
    
    def get_all(self):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM scada_scheme;
        ''')
        
        return cursor.fetchall()

    def update(self, scheme_id, new_name):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        UPDATE scada_scheme SET scheme_name = '{new_name}' WHERE scheme_id = {scheme_id}
        ''')
        self.__conn.commit()

    def delete(self, scheme_id: int):
        cursor = self.__conn.cursor()

        cursor.execute(f'''DELETE FROM scada_scheme WHERE scheme_ID = {scheme_id} ''')
        self.__conn.commit()
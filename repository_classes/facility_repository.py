from typing import List, Optional

from psycopg import Connection

from table_classes.facility import FacilityOut, FacilityIn, FacilityTypesOut, WorkshopOut, ScadaSchemeOut


class FacilityRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, new_facility: FacilityIn)-> FacilityOut:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO facility (facility_name, type_id, workshop_id, scada_scheme) VALUES (%s,%s,%s,%s)
        RETURNING facility_id, facility_name,type_id, workshop_id, scada_scheme
        ''', (new_facility.name, new_facility.type.type_ID, new_facility.workshop.workshop_id, new_facility.scada_schema.scheme_ID)
        )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()

        return FacilityOut(
            facility_id=fetched_row[0],
            name=fetched_row[1],
            type= new_facility.type.type_ID, 
            workshop= new_facility.workshop.workshop_id, 
            scada_schema= new_facility.scada_schema.scheme_ID
            )
        

    def get_by_ID(self, facility_id: str) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT workshop_id, workshop_name FROM workshop WHERE workshop_ID = %s''', (facility_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(fetched_row[0], fetched_row[1], type = fetched_row[2], workshop = fetched_row[3], scada_schema = fetched_row[4])
        else:
            return None
    
    
    def get_all(self) -> List[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                       SELECT f.facility_id, f.facility_name, t.type_id, t.type_name, w.workshop_id, w.workshop_name, s.scheme_id, s.scheme_name
                       FROM facility as f
                       ORDER BY facility_ID
                       USING JOIN facility_types as t ON t.type_id = f.type_id
                       USING JOIN workshop as w ON w.workshop_id = f.workshop_id
                       USING JOIN scada_scheme as s ON s.scheme_id = f.scheme_id
                       ''')
        
        result = []        
        for record in cursor.fetchall():
            type = FacilityTypesOut()
            workshop = WorkshopOut()
            scada_scheme = ScadaSchemeOut()
            new_obj = FacilityOut(record[0], record[1],type = type, workshop = workshop, scada_schema = scada_scheme)
            result.append(new_obj)  
        return result


    def update(self, workshop_id: str, new_name: str) -> Optional[WorkshopOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE workshop SET workshop_name = %s WHERE workshop_id = %s
        RETURNING workshop_id, workshop_name;''', (new_name, workshop_id,)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return WorkshopOut(fetched_row[0], fetched_row[1])
        else:
            return None


    def delete(self, facility_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM facility WHERE facility_ID = %s''', (facility_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
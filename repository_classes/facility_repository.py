from typing import List, Optional

from psycopg import Connection

from table_classes.facility import FacilityOut, FacilityIn, FacilityTypeOut, WorkshopOut, ScadaSchemeOut


class FacilityRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, new_facility: FacilityIn)-> FacilityOut:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO facility (facility_name, facility_type_id, workshop_id, scada_scheme_id) VALUES (%s,%s,%s,%s)
        RETURNING facility_id, facility_name,facility_type_id, workshop_id, scada_scheme_id
        ''', (new_facility.name, new_facility.type.facility_type_ID, new_facility.workshop.workshop_id, new_facility.scada_scheme.scheme_ID,)
        )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()

        return FacilityOut(
            facility_id=fetched_row[0],
            name=fetched_row[1],
            type= new_facility.type.facility_type_ID, 
            workshop= new_facility.workshop.workshop_id, 
            scada_scheme= new_facility.scada_scheme.scheme_ID
            )
        

    def get_by_ID(self, facility_id: str) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT facility_id, facility_name, facility_type_id, workshop_id, scada_scheme_id FROM facility WHERE facility_ID = %s''', (facility_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                fetched_row[0],
                fetched_row[1], 
                type = fetched_row[2], 
                workshop = fetched_row[3], 
                scada_scheme = fetched_row[4]
                )
        else:
            return None
    
    
    def get_all(self) -> List[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                        SELECT facility_id, facility_name, facility_type_id, facility_type_name, workshop_id, 
                            workshop.workshop_name, scada_scheme.scheme_id, scada_scheme.scheme_name
                        FROM facility
                        JOIN facility_types USING (facility_type_id)
                        JOIN workshop USING (workshop_id)
                        JOIN scada_scheme ON facility.scada_scheme_id = scada_scheme.scheme_id
                        ORDER BY facility_ID;
                       ''')
        
        result = []        
        for record in cursor.fetchall():
            type = FacilityTypeOut(record[2],record[3])
            workshop = WorkshopOut(record[4],record[5])
            scada_scheme = ScadaSchemeOut(record[6],record[7])
            new_obj = FacilityOut(record[0], record[1],type = type, workshop = workshop, scada_scheme = scada_scheme)
            result.append(new_obj)  
        return result


    def update(self, facility_id: int, new_facility: FacilityIn) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE facility SET facility_name = %s, facility_type_id = %s, workshop_id = %s, scada_scheme.scheme_id = %s
        WHERE facility_id = %s

        RETURNING facility_id, facility_name
        ''', 
        (new_facility.name, new_facility.type.facility_type_ID, new_facility.workshop.workshop_id, new_facility.scada_scheme.scheme_ID, facility_id,)
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            type = new_facility.type
            workshop = new_facility.workshop
            scada_scheme = new_facility.scada_schema
            return FacilityOut(
                fetched_row[0], 
                fetched_row[1], 
                type, 
                workshop, 
                scada_scheme)
        else:
            return None


    def delete(self, facility_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM facility WHERE facility_ID = %s''', (facility_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
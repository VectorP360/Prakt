from typing import List, Optional

from psycopg import Connection

from schemas.scada_scheme import ScadaSchemeOut, ScadaSchemeIn, FacilityOut
from schemas.facility_types import FacilityTypeOut
from schemas.workshop import WorkshopOut

class ScadaSchemeRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, scheme_in: ScadaSchemeIn)-> Optional[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO scada_scheme (name, facility_id) VALUES (%s, %s)
        ON CONFLICT (scada_scheme_id) DO NOTHING
        RETURNING scada_scheme_id, name
        ''', (scheme_in.name, scheme_in.facility.facility_id)
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()
        if fetched_row:
            return ScadaSchemeOut(scheme_id = fetched_row[0],
                                name = fetched_row[1], 
                                facility = scheme_in.facility)
        return None
        

    def get_by_ID(self, scada_scheme_id: str) -> Optional[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                        SELECT scada_scheme_id, scada_scheme.name, facility.facility_id, facility.name,
                        facility_type.facility_type_id, facility_type.name, workshop.workshop_id, workshop.name 
                        FROM scada_scheme 
                        JOIN facility USING (facility_id)
                            JOIN facility_types ON facility.type_id = facility_types.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                        WHERE scada_scheme_id = %s''', (scada_scheme_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return ScadaSchemeOut(
                scheme_id = fetched_row[0], 
                name = fetched_row[1],
                facility = FacilityOut(
                    facility_id = fetched_row[2],
                    name = fetched_row[3],
                    type = FacilityTypeOut(
                        facility_type_id = fetched_row[4],
                        name = fetched_row[5]
                    ),
                    workshop = WorkshopOut(
                        workshop_id = fetched_row[6],
                        name = fetched_row[7]
                    )
                )
            )
        else:
            return None
    
    
    def get_all(self) -> List[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                        SELECT scada_scheme_id, scada_scheme.name, facility.facility_id, facility.name,
                        facility_type.facility_type_id, facility_type.name, workshop.workshop_id, workshop.name 
                        FROM scada_scheme 
                        JOIN facility USING (facility_id)
                            JOIN facility_types ON facility.type_id = facility_types.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                       ORDER BY scada_scheme_id;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = ScadaSchemeOut(
                scheme_id = record[0], 
                name = record[1],
                facility = FacilityOut(
                    facility_id = record[2],
                    name = record[3],
                    type = FacilityTypeOut(
                        facility_type_id = record[4],
                        name = record[5]
                    ),
                    workshop = WorkshopOut(
                        workshop_id = record[6],
                        name = record[7]
                    )
                )
            )
            result.append(new_obj)  
        return result


    def update(self, scada_scheme_id: str, scada_in: ScadaSchemeIn) -> Optional[ScadaSchemeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE scada_scheme SET name = %s, facility_id = %s WHERE scada_scheme_id = %s
        RETURNING scada_scheme_id, name;''', (scada_in.name, scada_in.facility , scada_scheme_id)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return ScadaSchemeOut(scheme_id = fetched_row[0], 
                                  name = fetched_row[1], 
                                  facility = scada_in.facility)
        else:
            return None


    def delete(self, scada_scheme_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM scada_scheme WHERE scada_scheme_id = %s''', (scada_scheme_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
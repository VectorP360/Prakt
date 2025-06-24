from typing import List, Optional

from psycopg import Connection

from schemas.facility import FacilityOut, FacilityIn, FacilityTypeOut, WorkshopOut


class FacilityRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, new_facility: FacilityIn)-> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO facility (facility_name, facility_type_id, workshop_id, scada_scheme_id) VALUES (%s,%s,%s,%s)
        RETURNING facility_id, name,facility_type_id, workshop_id
        ''', (new_facility.name, new_facility.type.facility_type_id, new_facility.workshop.workshop_id,)
        )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                facility_id=fetched_row[0],
                name=fetched_row[1],
                type= new_facility.type, 
                workshop= new_facility.workshop
                )
        return None
        

    def get_by_ID(self, facility_id: int) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                       SELECT facility_id, facility.name, type_id, facility_type.type_name, workshop_id, workshop.name 
                       FROM facility 
                        JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                        JOIN workshop USING (workshop_id)
                       WHERE facility_id = %s
                       ''', (facility_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                fetched_row[0],
                fetched_row[1], 
                type = FacilityTypeOut(
                    facility_type_id=fetched_row[2],
                    name = fetched_row[3]
                ), 
                workshop = WorkshopOut(
                    workshop_id= fetched_row[4],
                    name= fetched_row[5]
                )
                )
        else:
            return None
    

    def get_by_name(self, name: str) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                       SELECT facility_id, facility.name, type_id, facility_type.type_name, workshop_id, workshop.name 
                       FROM facility 
                        JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                        JOIN workshop USING (workshop_id)
                       WHERE facility.name = %s
                       ''', (name,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return FacilityOut(
                fetched_row[0],
                fetched_row[1], 
                type = FacilityTypeOut(
                    facility_type_id=fetched_row[2],
                    name = fetched_row[3]
                ), 
                workshop = WorkshopOut(
                    workshop_id= fetched_row[4],
                    name= fetched_row[5]
                )
                )
        else:
            return None

    
    def get_all(self) -> List[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                        SELECT facility_id, facility.name, facility_type_id, facility_type.type_name, workshop_id, 
                            workshop.name
                        FROM facility
                        JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                        JOIN workshop USING (workshop_id)
                        ORDER BY facility_id;
                       ''')
        
        result = []        
        for record in cursor.fetchall():
            type = FacilityTypeOut(record[2],record[3])
            workshop = WorkshopOut(record[4],record[5])
            new_obj = FacilityOut(record[0], record[1],type = type, workshop = workshop)
            result.append(new_obj)  
        return result


    def update(self, facility_id: int, new_facility: FacilityIn) -> Optional[FacilityOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE facility SET facility_name = %s, facility_type_id = %s, workshop_id = %s
        WHERE facility_id = %s

        RETURNING facility_id, facility_name
        ''', 
        (new_facility.name, new_facility.type.facility_type_id, new_facility.workshop.workshop_id, facility_id,)
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            type = new_facility.type
            workshop = new_facility.workshop
            return FacilityOut(
                fetched_row[0], 
                fetched_row[1], 
                type, 
                workshop)
        else:
            return None


    def delete(self, facility_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM facility WHERE facility_id = %s''', (facility_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
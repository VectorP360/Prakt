from typing import List, Optional

from psycopg import Connection

from schemas.conditions import ConditionsIn, ConditionsOut
from schemas.facility import FacilityOut
from schemas.facility_types import FacilityTypeOut
from schemas.workshop import WorkshopOut

class ConditionsRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, condition_in: ConditionsIn) -> Optional[ConditionsOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            INSERT INTO element (temprature, loading, pressure, facility) VALUES (%s, %s, %s, %s)
            RETURNING (condition_id, temperature, loading, pressure)
            """, (condition_in.temperature, condition_in.loading, condition_in.pressure, condition_in.facility.facility_id)
            )
        
        self.__connection.commit()

        fetched_row = cursor.fetchone()
        if fetched_row:
            return ConditionsOut(condition_id = fetched_row[0],
                              temperature = fetched_row[1],
                              loading = fetched_row[2],
                              pressure = fetched_row[3],
                              facility = condition_in.facility)
        return None
    
    def get_by_id(self, condition_id: int) -> Optional[ConditionsOut]:

        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT condition_id, temperature, loading, pressure, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.type_name, 
                    workshop.workshop_id, workshop.name
            FROM conditions
                JOIN facility ON conditions.facility = facility.facility_id
                JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                JOIN workshop ON facility.workshop_id = workshop.workshop_id
            WHERE condition_id = %s
            """, (condition_id,)
            )
        fetched_row = cursor.fetchone()

        if fetched_row:
            return ConditionsOut(
                condition_id = fetched_row[0],
                temperature = fetched_row[1],
                loading = fetched_row[2],
                pressure = fetched_row[3],
                facility = FacilityOut(
                    facility_id = fetched_row[4],
                    name = fetched_row[5],
                    type = FacilityTypeOut(
                        facility_type_id = fetched_row[6],
                        name = fetched_row[7]
                        ), 
                        workshop = WorkshopOut(
                            workshop_id = fetched_row[8],
                            name = fetched_row[9]
                        )
                    ) 
                )
        else:
            return None
    
    def get_by_user(self, user_id:int)-> Optional[ConditionsOut]:

        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT condition_id, temperature, loading, pressure, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.type_name, 
                    workshop.workshop_id, workshop.name
            FROM conditions
                JOIN facility ON conditions.facility = facility.facility_id
                JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                JOIN workshop ON facility.workshop_id = workshop.workshop_id
                JOIN users on facility.facility_id = users.facility_id
            WHERE users.user_id = %s
            """, (user_id,)
            )
        
        fetched_row = cursor.fetchone()

        if fetched_row:
            return ConditionsOut(
                condition_id = fetched_row[0],
                temperature = fetched_row[1],
                loading = fetched_row[2],
                pressure = fetched_row[3],
                facility = FacilityOut(
                    facility_id = fetched_row[4],
                    name = fetched_row[5],
                    type = FacilityTypeOut(
                        facility_type_id = fetched_row[6],
                        name = fetched_row[7]
                        ), 
                        workshop = WorkshopOut(
                            workshop_id = fetched_row[8],
                            name = fetched_row[9]
                        )
                    ) 
                )
        else:
            return None
    
    def get_all(self) -> Optional[list]:

        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT condition_id, temperature, loading, pressure, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.type_name, 
                    workshop.workshop_id, workshop.name
            FROM conditions
                JOIN facility ON conditions.facility = facility.facility_id
                JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                JOIN workshop ON facility.workshop_id = workshop.workshop_id
                JOIN users on facility.facility_id = users.facility_id
            """
            )
        
        fetched_row = cursor.fetchall()

        result = []
        if fetched_row:
            for cell in fetched_row:
                founded_condition = ConditionsOut(
                    condition_id = fetched_row[0],
                    temperature = fetched_row[1],
                    loading = fetched_row[2],
                    pressure = fetched_row[3],
                    facility = FacilityOut(
                        facility_id = fetched_row[4],
                        name = fetched_row[5],
                        type = FacilityTypeOut(
                            facility_type_id = fetched_row[6],
                            name = fetched_row[7]
                            ), 
                            workshop = WorkshopOut(
                                workshop_id = fetched_row[8],
                                name = fetched_row[9]
                            )
                        ) 
                    )
                
                result.append(founded_condition)
            return result
        else:
            return None
    
    def update(self, condition_id: int, new_condition: ConditionsIn) -> Optional[ConditionsOut]:

        cursor = self.__connection.cursor()

        cursor.execute(
            """
            UPDATE conditions SET temperature = %s, loading = %s, pressure = %s, facility = %s
            WHERE conditions.condition_id = %s

            RETURNING condition_id, temperature, loading, pressure, facility
            """,(new_condition.temperature, new_condition.loading, new_condition.pressure, new_condition.facility.facility_id, condition_id,)
            )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()

        if fetched_row:
            
            facility = new_condition.facility

            return ConditionsOut(
                condition_id = fetched_row[0],
                temperature = fetched_row[1],
                loading = fetched_row[2],
                pressure = fetched_row[3],
                facility = facility 
                )
        else:
            return None
        
    def delete(self, condition_id: int) -> bool:

        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM conditions WHERE condition_id = %s''', (condition_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
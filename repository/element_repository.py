from typing import List, Optional

from psycopg import Connection

from schemas.element import ElementIn, ElementOut

class ElementRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, element_in: ElementIn) -> Optional[ElementOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            INSERT INTO element (name, material, element_type, facility_id) VALUES (%s, %s, %s, %s)
            RETURNING (element_id, name, material)
            """, (element_in.name, element_in.material, element_in.element_type.element_type_id, element_in.facility.facility_id)
            )
        
        self.__connection.commit()

        fetched_row = cursor.fetchone()
        if fetched_row:
            return ElementOut(element_id = fetched_row[0],
                              name = fetched_row[1],
                              material = fetched_row[2],
                              element_type = element_in.element_type,
                              facility_id = element_in.facility)
        return None
    
    def get_by_id(self):

        return None
    
    def get_all(self):

        return None
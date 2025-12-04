from typing import Optional

from psycopg import Connection

from src.schemas.element import ElementIn, ElementOut
from src.schemas.element_type import ElementTypeOut
from src.schemas.facility import FacilityOut
from src.schemas.facility_type import FacilityTypeOut
from src.schemas.workshop import WorkshopOut


class ElementRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, element_in: ElementIn) -> Optional[ElementOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            INSERT INTO element (name, material, element_type_id, facility_id) VALUES (%s, %s, %s, %s)
            RETURNING (element_id, name, material)
            """,
            (
                element_in.name,
                element_in.material,
                element_in.element_type.element_type_id,
                element_in.facility.facility_id,
            ),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()
        if fetched_row:
            return ElementOut(
                element_id=fetched_row[0],
                name=fetched_row[1],
                material=fetched_row[2],
                element_type=element_in.element_type,
                facility_id=element_in.facility,
            )
        return None

    def get_by_id(self, element_id: int) -> Optional[ElementOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT element_id, element.name, material, element_type.element_type_id, element_type.name , facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                    workshop.workshop_id, workshop.name
            FROM element
                JOIN element_type ON element.element_type_id = element_type.element_type_id
                JOIN facility ON element.facility = facility.facility_id
                JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                JOIN workshop ON facility.workshop_id = workshop.workshop_id
            WHERE element_id = %s
            """,
            (element_id,),
        )
        fetched_row = cursor.fetchone()

        if fetched_row:
            return ElementOut(
                element_id=fetched_row[0],
                name=fetched_row[1],
                material=fetched_row[2],
                element_type=ElementTypeOut(
                    element_type_id=fetched_row[3], name=fetched_row[4]
                ),
                facility=FacilityOut(
                    facility_id=fetched_row[5],
                    name=fetched_row[6],
                    type=FacilityTypeOut(
                        facility_type_id=fetched_row[7], name=fetched_row[8]
                    ),
                    workshop=WorkshopOut(
                        workshop_id=fetched_row[9], name=fetched_row[10]
                    ),
                ),
            )
        else:
            return None

    def get_by_user(self, user_id: int) -> list:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT element_id, element.name, material, element_type.element_type_id, element_type.name , facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                    workshop.workshop_id, workshop.name
            FROM element
                JOIN element_type ON element.element_type_id = element_type.element_type_id
                JOIN facility ON element.facility_id = facility.facility_id
                JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                JOIN workshop ON facility.workshop_id = workshop.workshop_id
                JOIN public.user on facility.facility_id = public.user.facility_id
            WHERE public.user.user_id = %s
            """,
            (user_id,),
        )
        fetched_rows = cursor.fetchall()

        result = []
        for row in fetched_rows:
            founded_element = ElementOut(
                element_id=row[0],
                name=row[1],
                material=row[2],
                element_type=ElementTypeOut(element_type_id=row[3], name=row[4]),
                facility=FacilityOut(
                    facility_id=row[5],
                    name=row[6],
                    type=FacilityTypeOut(facility_type_id=row[7], name=row[8]),
                    workshop=WorkshopOut(workshop_id=row[9], name=row[10]),
                ),
            )

            result.append(founded_element)
        return result

    def get_all(self) -> Optional[list]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT element_id, element.name, material, element_type.element_type_id, element_type.name , facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                    workshop.workshop_id, workshop.name
            FROM element
                JOIN element_type ON element.element_type_id = element_type.element_type_id
                JOIN facility ON element.facility = facility.facility_id
                JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                JOIN workshop ON facility.workshop_id = workshop.workshop_id
            """
        )

        fetched_row = cursor.fetchall()

        result = []
        if fetched_row:
            for cell in fetched_row:
                founded_element = ElementOut(
                    element_id=cell[0],
                    name=cell[1],
                    material=cell[2],
                    element_type=ElementTypeOut(element_type_id=cell[3], name=cell[4]),
                    facility=FacilityOut(
                        facility_id=cell[5],
                        name=cell[6],
                        type=FacilityTypeOut(facility_type_id=cell[7], name=cell[8]),
                        workshop=WorkshopOut(workshop_id=cell[9], name=cell[10]),
                    ),
                )

                result.append(founded_element)
            return result
        else:
            return None

    def update(self, element_id: int, new_element: ElementIn) -> Optional[ElementOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            UPDATE element SET name = %s, material = %s, element_type_id = %s, facility_id = %s
            WHERE element.element_id = %s

            RETURNING element_id, name, material, element_type, facility
            """,
            (
                new_element.name,
                new_element.material,
                new_element.element_type.element_type_id,
                new_element.facility.facility_id,
                element_id,
            ),
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            element_type = new_element.element_type
            facility = new_element.facility

            return ElementOut(
                element_id=fetched_row[0],
                name=fetched_row[1],
                material=fetched_row[2],
                element_type=element_type,
                facility=facility,
            )
        else:
            return None

    def delete(self, element_id: int) -> bool:
        cursor = self.__connection.cursor()

        cursor.execute("""DELETE FROM element WHERE element_id = %s""", (element_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)

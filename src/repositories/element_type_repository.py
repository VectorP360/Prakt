from typing import List, Optional

from psycopg import Connection

from src.schemas.element_type import ElementTypeOut


class ElementTypeRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, name: str) -> Optional[ElementTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
        INSERT INTO element_type (name) VALUES (%s)
        ON CONFLICT (element_type_id) DO NOTHING
        RETURNING element_type_id, name
        """,
            (name,),
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()
        if fetched_row:
            return ElementTypeOut(fetched_row[0], fetched_row[1])
        return None

    def get_by_ID(self, type_id: str) -> Optional[ElementTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """SELECT element_type_id, name FROM element_type WHERE element_type_id = %s""",
            (type_id,),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return ElementTypeOut(fetched_row[0], fetched_row[1])
        else:
            return None

    def get_all(self) -> List[ElementTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """SELECT element_type_id, name FROM element_type ORDER BY element_type_id;"""
        )

        result = []
        for record in cursor.fetchall():
            new_obj = ElementTypeOut(record[0], record[1])
            result.append(new_obj)
        return result

    def update(self, type_id: str, new_name: str) -> Optional[ElementTypeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
        UPDATE element_type SET name = %s WHERE element_type_id = %s
        RETURNING element_type_id, name;""",
            (
                new_name,
                type_id,
            ),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return ElementTypeOut(fetched_row[0], fetched_row[1])
        else:
            return None

    def delete(self, type_id: int) -> bool:
        cursor = self.__connection.cursor()

        cursor.execute(
            """DELETE FROM element_type WHERE element_type_id = %s""", (type_id,)
        )
        self.__connection.commit()

        return bool(cursor.rowcount)

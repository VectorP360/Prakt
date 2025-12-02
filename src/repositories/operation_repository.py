from typing import Optional

from psycopg import Connection

from schemas.operation import OperationIn, OperationOut

class OperationRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, operation_in: OperationIn) -> Optional[OperationOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            INSERT INTO operation (name) VALUES (%s)
            RETURNING (operation_id, name)
            """,
            (
                operation_in.name,
            ),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()
        if fetched_row:
            return OperationOut(
                operation_id=fetched_row[0],
                name=fetched_row[1]
            )
        return None
    
    def get_by_id(self, operation_id: int) -> Optional[OperationOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT operation_id, name FROM operation WHERE operation_id = %s
            """,
            (operation_id,),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return OperationOut(
                operation_id=fetched_row[0],
                name=fetched_row[1]
            )
        return None
    
    def get_by_name(self, name: str):
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT operation_id, name FROM operation WHERE name = %s
            """,
            (name,),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return OperationOut(
                operation_id=fetched_row[0],
                name=fetched_row[1]
            )
        return None
    
    def get_all(self) -> Optional[list]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT operation_id, name FROM operation
            """
        )

        result = []
        for record in cursor.fetchall():
            new_obj = OperationOut(record[0],record[1])
            result.append(new_obj)

        return result
    
    def update(self, operation_id: int, new_operation: OperationIn) -> Optional[OperationOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            UPDATE operation SET name = %s WHERE  operation_id = %s
            """,
            (new_operation.name, operation_id,),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return OperationOut(
                operation_id=fetched_row[0],
                name=fetched_row[1]
            )
        else:
            return None
        
    def delete(self, operation_id: int) -> bool:
        cursor = self.__connection.cursor()

        cursor.execute(
            """DELETE FROM operstion WHERE operation_id = %s""",
            (operation_id,),
        )
        self.__connection.commit()

        return bool(cursor.rowcount)
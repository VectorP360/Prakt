from typing import List, Optional

from psycopg import Connection

from schemas.post import PostOut, PostIn


class PostRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, name: str) -> PostIn:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
        INSERT INTO post (name) VALUES (%s)
        ON CONFLICT (post_id) DO NOTHING
        """,
            (name,),
        )
        self.__connection.commit()

        return PostIn(name)

    def get_by_ID(self, post_id: str) -> Optional[PostOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """SELECT post_id, name FROM post WHERE post_ID = %s""", (post_id,)
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return PostOut(fetched_row[0], fetched_row[1])
        else:
            return None

    def get_by_name(self, name: str) -> Optional[PostOut]:
        cursor = self.__connection.cursor()

        cursor.execute("""SELECT post_id, name FROM post WHERE name = %s""", (name,))

        fetched_row = cursor.fetchone()

        if fetched_row:
            return PostOut(fetched_row[0], fetched_row[1])
        else:
            return None

    def get_all(self) -> List[PostOut]:
        cursor = self.__connection.cursor()

        cursor.execute("""SELECT post_id, name FROM post ORDER BY post_ID;""")

        result = []
        for record in cursor.fetchall():
            new_obj = PostOut(record[0], record[1])
            result.append(new_obj)
        return result

    def update(self, post_id: str, new_name: str) -> Optional[PostOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
        UPDATE post SET name = %s WHERE post_id = %s
        RETURNING post_id, name;""",
            (
                new_name,
                post_id,
            ),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return PostOut(fetched_row[0], fetched_row[1])
        else:
            return None

    def delete(self, post_id: int) -> bool:
        cursor = self.__connection.cursor()

        cursor.execute("""DELETE FROM post WHERE post_ID = %s""", (post_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)

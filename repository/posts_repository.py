from typing import List, Optional

from psycopg import Connection

from schemas.posts import PostsOut, PostsIn

class PostsRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, post_name: str)-> PostsIn:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO posts (post_name) VALUES (%s)
        ON CONFLICT (post_id) DO NOTHING
        ''', (post_name,)
        )
        self.__connection.commit()
        
        return PostsIn(post_name)
        

    def get_by_ID(self, post_id: str) -> Optional[PostsOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT post_id, post_name FROM posts WHERE post_ID = %s''', (post_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return PostsOut(fetched_row[0], fetched_row[1])
        else:
            return None
    
    
    def get_all(self) -> List[PostsOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT post_id, post_name FROM posts ORDER BY post_ID;''')
        
        result = []        
        for record in cursor.fetchall():
            new_obj = PostsOut(record[0], record[1])
            result.append(new_obj)  
        return result


    def update(self, post_id: str, new_name: str) -> Optional[PostsOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE posts SET post_name = %s WHERE post_id = %s
        RETURNING post_id, post_name;''', (new_name, post_id,)
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return PostsOut(fetched_row[0], fetched_row[1])
        else:
            return None


    def delete(self, post_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM posts WHERE post_ID = %s''', (post_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
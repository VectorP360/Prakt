import psycopg
import table_classes.posts as posts

class PostsRepository:
    def __init__(self, connection: psycopg.Connection):
        self.__conn = connection

    def create(self, post_id: int, post_name: str):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        INSERT INTO posts (post_id, post_name) VALUES ({post_id}, '{post_name}');
        ''')

        self.__conn.commit()
        return posts.Posts(post_id, post_name)


    def get_by_ID(self, post_id):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM posts WHERE post_id = {post_id};
        ''')
        
        return cursor.fetchall()
    
    def get_all(self):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        SELECT * FROM posts;
        ''')
        
        return cursor.fetchall()

    def update(self, post_id, new_name):
        cursor = self.__conn.cursor()

        cursor.execute(f'''
        UPDATE posts SET post_name = '{new_name}' WHERE post_id = {post_id}
        ''')
        self.__conn.commit()

    def delete(self, post_id: int):
        cursor = self.__conn.cursor()

        cursor.execute(f'''DELETE FROM posts WHERE post_ID = {post_id} ''')
        self.__conn.commit()
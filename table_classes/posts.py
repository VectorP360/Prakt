class PostsOut:
    def __init__(self, post_ID: int, post_name: str):
        self.post_ID = post_ID
        self.post_name = post_name

class PostsIn:
    def __init__(self, post_name: str):
        self.post_name = post_name
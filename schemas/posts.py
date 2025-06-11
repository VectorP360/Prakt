class PostsOut:
    def __init__(self, post_ID: int, name: str):
        self.post_ID = post_ID
        self.name = name

class PostsIn:
    def __init__(self, name: str):
        self.name = name
class PostOut:
    def __init__(self, post_ID: int, name: str):
        self.post_ID = post_ID
        self.name = name

    def __str__(self):
        return f'id должности: {self.post_ID}, название должности: {self.name}'

class PostIn:
    def __init__(self, name: str):
        self.name = name
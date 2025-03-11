import uuid




class News:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.id = str(uuid.uuid4())
    def __str__(self):
        return f"{self.title}\n\n\n{self.content}\n{self.id}\n"
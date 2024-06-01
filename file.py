from datetime import datetime


class File:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content
        self.date_create = datetime.now()

    def cat(self):
        return self.name

    @property
    def information(self):
        return f"file: {self.name}"

    @property
    def __str__(self):
        return self.name




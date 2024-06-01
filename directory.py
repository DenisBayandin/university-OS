

class Directory:
    def __init__(self, name: str):
        self.files = []
        self.sub_directories = {}
        self.name = name

    @property
    def information(self):
        return f"directory: {self.name}"

    @property
    def __str__(self):
        return self.name
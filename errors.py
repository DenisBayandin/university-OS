from constants import VALID_COUNT_SYMBOLS, VALID_COUNT_SYMBOLS_FOR_CONTENT


class NotFoundDirectory(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Not found directory {self.name}"


class InvalidCountSymbols(Exception):
    def __str__(self):
        return f"Invalid count symbols. Max symbols for name and content: {VALID_COUNT_SYMBOLS}," \
               f" {VALID_COUNT_SYMBOLS_FOR_CONTENT}"


class InvalidSymbolInName(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Invalid symbol in {self.name}"


class NotFoundExtension(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Invalid file extension {self.name}"


class InvalidFileExtension(Exception):
    def __init__(self, extension):
        self.extension = extension

    def __str__(self):
        return f"Invalid file extension {self.extension}"


class NotFoundFile(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Not found name {self.name}"

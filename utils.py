from constants import VALID_COUNT_SYMBOLS, INVALID_SYMBOLS, VALID_FILE_EXTENSION, VALID_COUNT_SYMBOLS_FOR_CONTENT
from errors import *


def check_valid_length(func):
    def wrapper(object, name, *args, **kwargs):
        if len(name) > VALID_COUNT_SYMBOLS:
            raise InvalidCountSymbols
        func(object, name, *args, **kwargs)
    return wrapper


def check_having_invalid_symbols(func):
    def wrapper(object, name, *args, **kwargs):
        for symbol in INVALID_SYMBOLS:
            if symbol in name:
                raise InvalidSymbolInName(name)
        func(object, name, *args, **kwargs)
    return wrapper


def check_valid_file_extension(func):
    def wrapper(object, name, content, *args, **kwargs):
        if len(name.split(".")) != 2:
            raise NotFoundExtension(name)
        if name.split(".")[1] not in VALID_FILE_EXTENSION:
            raise InvalidFileExtension(name.split(".")[1])
        func(object, name, content, *args, **kwargs)
    return wrapper


def check_valid_length_content(func):
    def wrapper(object, name, content, *args, **kwargs):
        if len(content) > VALID_COUNT_SYMBOLS_FOR_CONTENT:
            raise InvalidCountSymbols
        func(object, name, content, *args, **kwargs)
    return wrapper

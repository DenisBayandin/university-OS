from utils import check_valid_length, check_having_invalid_symbols,\
    check_valid_file_extension, check_valid_length_content
from directory import Directory
from file import File
from errors import NotFoundFile


class System:
    def __init__(self):
        self.system = []
        self.current_state = None

    @check_valid_length
    @check_valid_file_extension
    @check_valid_length_content
    def touch(self, name: str, content: str):
        self.system.append(File(name=name, content=content))

    @property
    def ls(self):
        return "; ".join([object_system.information for object_system in self.system])

    def rm(self, name: str):
        try:
            self.system.pop([object_name.name for object_name in self.system].index(name))
        except ValueError:
            raise NotFoundFile(name)

    def search_file(self, name: str):
        return "; ".join([f"{index}. Name: {file.name}, date create: {file.date_create}" for
                          index, file in enumerate(self.system, start=1) if name in file.name])

    def cat(self, name: str):
        try:
            return self.system[[object_name.name for object_name in self.system].index(name)].content
        except ValueError:
            raise NotFoundFile(name)

    # @property
    # def current_state_is_home(self):
    #     return True if self.current_state is None else False

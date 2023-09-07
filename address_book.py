from collections import UserDict


class Field:
    def __init__(self, name: str):
        self.name = name


class Name(Field):
    def __init__(self, value: str):
        self.value = value


class Phone(Field):
    def __init__(self, value: str):
        list_values = []
        if value:
            list_values.append(value)
        self.value = list_values


class Record:
    
    def __init__(self, name, phone=''):
        self.name = Name(name)
        self.phone = Phone(phone)
    
    def add_phone(self, phone):
        pass
        # self.phone.


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data.update(record)










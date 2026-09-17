from field import *

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __find(self, phone: str,get_instance: bool = False) -> int | Phone | None:
        #якщо пошук з двома аргументами - повертає значення, інакше позицію входження
        for id, instance in enumerate(self.phones):
            if instance.value == phone:
                return instance if get_instance else id
        return None

    def add_phone(self, phone : str):

        if self.__find(phone,True):
             # If already exists - do nothing
             pass
        else:
            self.phones.append(Phone(phone))

    def find_phone(self, phone : str):
        return self.__find(phone, True)

    def remove_phone (self, phone :str):
        if (id := self.__find(phone)) is not None:
            del self.phones[id]

    def edit_phone(self, old: str, new : str):
        if (id := self.__find(old)) is None:
            raise ValueError(f'Phone {old} not found!')
        else:
            self.phones[id] = Phone(new)

    def add_birthday(self, bday:str):
        if not self.birthday:
            self.birthday = Birthday(bday)

    def __str__(self):
        return f"Contact name: {self.name.value}, Birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"

# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday('16.09.2015')
# print(john_record.birthday)

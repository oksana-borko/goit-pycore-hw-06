
from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value.strip())


class Phone(Field):

    def __init__(self, value: str):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError(f"Invalid phone number '{value}': must be exactly 10 digits.")
        super().__init__(value)


class Record:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str) -> None:

        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> Phone | None:

        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str) -> None:

        found = self.find_phone(phone)
        if found is None:
            raise ValueError(f"Phone '{phone}' not found.")
        self.phones.remove(found)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        found = self.find_phone(old_phone)
        if found is None:
            raise ValueError(f"Phone '{old_phone}' not found.")
        new = Phone(new_phone)
        index = self.phones.index(found)
        self.phones[index] = new

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):


    def add_record(self, record: Record) -> None:

        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:

        return self.data.get(name)

    def delete(self, name: str) -> None:

        if name not in self.data:
            raise KeyError(f"Contact '{name}' not found.")
        del self.data[name]


if __name__ == "__main__":

    book = AddressBook()


    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")


    book.add_record(john_record)


    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)


    for name, record in book.data.items():
        print(record)


    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)


    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")
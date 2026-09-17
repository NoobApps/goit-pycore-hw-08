from book import AddressBook
from record import Record
from field import *
from utils import input_error
import pickle


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    if len(args)< 2:
        raise ValueError("Please type add name phone")
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    if len(args) != 3 or not Phone(args[1]).value or not Phone(args[2]).value:
        raise ValueError("Invalid input. Use 'change [name] [old_phone] [new_phone]'")
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
    return "Contact updated"

@input_error
def get_phone(args,book):

    name, *_ = args
    record=book.find(name)
    if record:
        user_phones=[]
        for phone in record.phones:
           user_phones.append(phone.value)
        return f"{name}'s phone numbers: {"; ".join(user_phones)}"
    else:
        return "Not Found"


def get_all(args,book):
    return book

@input_error
def add_birthday(args, book):
    name, bday,*_ = args
    record = book.find(name)
    if record.birthday is None:
        record.add_birthday(bday)
    return f"Birthday at {record.birthday} added for {name}"

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if not record.birthday is None:
        return f"{name}'s birthday is at {record.birthday}"

def birthdays(args, book):
    return book.get_upcoming_birthdays()

def save_data(book, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if len(user_input.strip())==0:
            print("No command entered: try [hello, add, change, all, phone, add-birthday, show-birthday, birthdays]")
            continue
        else:
            command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print (book)
            save_data(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command=="change":
            print(change_contact(args,book))
        elif command=="phone":
            print(get_phone(args,book))
        elif command=="all":
            print(get_all(args,book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()


from book import AddressBook
from record import Record
from field import *
from handlers import *


HANDLERS = {
    'add' : add_contact,
    'hello': hello,
    'change' :change_contact,
    'phone' : get_phone,
    'all' : get_all,
    'add-birthday' : add_birthday,
    'show-birthday' : show_birthday,
    'birthdays' : birthdays
}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if len(user_input.strip())==0:
            print(f"No command entered: try {HANDLERS.keys()}")
            continue
        else:
            command, *args = parse_input(user_input)

        if command in HANDLERS.keys():
            print (HANDLERS.get(command)(args, book))

        elif command in ["close", "exit"]:
            print (book)
            save_data(book)
            print("Good bye!")
            break

        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()


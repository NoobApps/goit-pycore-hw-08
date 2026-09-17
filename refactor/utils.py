from field import *
from functools import wraps


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            if func.__name__ == "add_contact":
                return ValueError("Invalid input. Use 'add [name] [10 digits phone]'")
            elif func.__name__ == "change_contact":
                return ValueError("Invalid input. Use 'change [name] [old_phone] [new_phone]'")
            elif func.__name__ == "get_phone":
                return ValueError("Invalid input. Use 'phone [name]'")
            elif func.__name__ == "add_birthday":
                return ValueError("Invalid input. Use 'add-birthday [name] [date of birth in DD.MM.YYYY format]'")
            elif func.__name__ == "show_birthday":
                return ValueError("Invalid input. Use 'show-birthday [name]'")
            else:
                return ValueError("Invalid command")
            
        


    return wrapper
    
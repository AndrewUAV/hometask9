import re

INFO_ABOUT_USERS = dict()

def func_hello():
    """
    function of reaction on input 'hello'
    :return: str
    """
    return 'How can I help you?'


def validate_phone_number(phone_number):
    """
    function for check valid phone number
    :param phone_number: like +380651329565
    :return: True if valid
    """
    pattern = '^[+][0-9]{12}$'
    if re.match(pattern, phone_number):
        return True
    else:
        raise ValueError('Invalid phone number format.')

def func_add(name_and_number):
    """
    function for add new user
    :param name_and_number: str name + phone
    :return: save info in INFO_ABOUT_USERS and return message if successfull
    """
    name, phone_number = map(str.strip, name_and_number.split(" "))

    if name in INFO_ABOUT_USERS:
        raise ValueError('Contact already exists. Use "change" command to update the phone number.')

    validate_phone_number(phone_number)

    INFO_ABOUT_USERS[name] = phone_number
    return "Info saved successfully."

def func_change(name_and_number):
    """
    function for change phone number of some user
    :param name_and_number: str name + phone number
    :return: message if successfull
    """
    name, phone_number = map(str.strip, name_and_number.split(" "))

    if name not in INFO_ABOUT_USERS:
        raise KeyError('The contact is missing. Use "add" command to add a new contact.')

    validate_phone_number(phone_number)

    INFO_ABOUT_USERS[name] = phone_number
    return "Info saved successfully."

def func_phone(name):
    """
    function for return number of user
    :param name: user
    :return: phone number
    """
    if name in INFO_ABOUT_USERS:
        return INFO_ABOUT_USERS[name]
    else:
        raise KeyError('The contact is missing.')

def func_show_all(info_about_users):
    """
    function for show all information about users
    :param info_about_users: dict
    :return: all info
    """
    if info_about_users:
        return [f"{name}: {phone_number}" for name, phone_number in info_about_users.items()]
    else:
        return ['The contact list is empty.']

def func_quit():
    """
    function for quit
    :return: messages if bot is not active
    """
    return "Good bye!"

def input_error(func):
    # function for check errors
    def inner():
        while True:
            try:
                result = func()
                break
            except IndexError:
                print('Enter the name and number separated by a space.')
            except ValueError as ve:
                print(f'Error: {ve}')
            except KeyError as ke:
                print(f'Error: {ke}')
        return result

    return inner

@input_error
def main():

    while True:
        command = input("Enter a valid command: ").lower()
        if command == 'hello':
            print(func_hello())
        elif command.startswith('add'):
            print(func_add(command.removeprefix('add').strip()))
        elif command.startswith('change'):
            print(func_change(command.removeprefix('change').strip()))
        elif command.startswith('phone'):
            print(func_phone(command.removeprefix('phone').strip()))
        elif command == "show all":
            contacts = func_show_all(INFO_ABOUT_USERS)
            for contact in contacts:
                print(contact)
        elif command in ["good bye", "close", "exit"]:
            print(func_quit())
            break
        else:
            print("Enter a correct command, please.")

if __name__ == '__main__':
    main()

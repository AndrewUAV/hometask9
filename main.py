import re

info_about_users = dict()

def input_error(func):
    def inner(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                break
            except AttributeError:
                return 'Enter the name and number separated by a space.'
            except ValueError as ve:
                return f'Error: {ve}'
            except KeyError as ke:
                return f'Error: {ke}'
        return result
    return inner

@input_error
def parser_command(command):
    if command == 'hello':
        return func_hello()

    elif command.startswith('add ') and len(command.split(' ')) == 3:
        return func_add(command.removeprefix('add').strip())

    elif command.startswith('change ') and len(command.split(' ')) == 3:
        return func_change(command.removeprefix('change').strip())

    elif command.startswith('phone ') and len(command.split(' ')) == 2:
        return func_phone(command.removeprefix('phone').strip())

    elif command == "show all":
        contacts = func_show_all()

        for contact in contacts:
            print(contact)

    elif command in ["good bye", "close", "exit"]:
        return func_quit()
    else:
        return "Invalid command. Please enter a valid command."

def func_hello():
    return 'How can I help you?'

def validate_phone_number(phone_number):
    pattern = '^[+][0-9]{12}$'
    return bool(re.match(pattern, phone_number))
    
@input_error
def func_add(name_and_number):
    name, phone_number = map(str.strip, name_and_number.split(" "))
    if validate_phone_number(phone_number):
        info_about_users[name] = phone_number
        return "Info saved successfully."
    else:
        return "Invalid phone format"
        
@input_error
def func_change(name_and_number):
    name, phone_number = map(str.strip, name_and_number.split(" "))
    if validate_phone_number(phone_number):
        info_about_users[name] = phone_number
        return "Info saved successfully."
    else:
        return "Invalid phone format"

@input_error
def func_phone(name):
    return info_about_users.get(name, f'The contact "{name}" is missing.')

@input_error
def func_show_all():
    if info_about_users:
        return [f"{name}: {phone_number}" for name, phone_number in info_about_users.items()]
    else:
        return ['The contact list is empty.']


def func_quit():
    return "Good bye!"

def func_help():
    # function for create start message with help
    return ('Hi! If you want start work just enter "hello"\n' +
            'Number phone start with +38 for UA\n' +
            'The representation of all commands looks as follows:\n' +
            '"hello" - start work with bot\n' +
            '"add" name phone\n' +
            '"change" name phone\n' +
            '"phone" name\n' +
            '"show all" - for show all information\n' +
            '"good bye", "close", "exit" - for end work')

def main():
    # print list help
    print(func_help())

    while True:

        command = input('Please, enter the valid command: ')
        print(parser_command(command))
        if command in ['exit', 'good bye', 'close']:
            break

if __name__ == '__main__':
    main()

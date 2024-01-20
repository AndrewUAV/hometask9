import re

info_about_users = {'Andrew': '+380660951381'}

def input_error(func):
    def inner():
        while True:
            try:
                result = func()
                break
            except IndexError:
                return 'Enter the name and number separated by a space.'
            except ValueError as ve:
                return f'Error: {ve}'
            except KeyError as ke:
                return f'Error: {ke}'
            except Exception as e:
                return f'Unexpected error: {e}'
        return result

    return inner

def func_hello():
    return 'How can I help you?'

def validate_phone_number(phone_number):
    pattern = '^[+][0-9]{12}$'
    return bool(re.match(pattern, phone_number))

def func_add(name_and_number):
    name, phone_number = map(str.strip, name_and_number.split(" "))

    if name in info_about_users:
        return 'Contact already exists. Use "change" command to update the phone number.'

    if not validate_phone_number(phone_number):
        return 'Invalid phone number format. Try again.'

    info_about_users[name] = phone_number
    return "Info saved successfully."

def func_change(name_and_number):
    name, phone_number = map(str.strip, name_and_number.split(" "))

    if name not in info_about_users:
        return 'The contact is missing. Use "add" command to add a new contact.'

    if not validate_phone_number(phone_number):
        return 'Invalid phone number format.'

    info_about_users[name] = phone_number
    return "Info saved successfully."

def func_phone(name):
    return info_about_users.get(name, 'The contact is missing.')

def func_show_all():
    if info_about_users:
        return [f"{name}: {phone_number}" for name, phone_number in info_about_users.items()]
    else:
        return ['The contact list is empty.']

def func_quit():
    return "Goodbye!"

def get_help():
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
@input_error
def main():

    # write help messages
    print(get_help())

    # the main cycle of work
    while True:
        command = input("Enter a valid command: ").lower()

        if command == 'hello':
            print(func_hello())

        elif command.startswith('add') and len(command.split(' ')) == 3:
            print(func_add(command.removeprefix('add').strip()))

        elif command.startswith('change') and len(command.split(' ')) == 3:
            print(func_change(command.removeprefix('change').strip()))

        elif command.startswith('phone') and len(command.split(' ')) == 2:
            print(func_phone(command.removeprefix('phone').strip()))

        elif command == "show all":
            contacts = func_show_all()

            for contact in contacts:
                print(contact)

        elif command in ["good bye", "close", "exit"]:
            print(func_quit())
            break

        else:
            print("Enter a correct command, please.")

if __name__ == '__main__':
    main()

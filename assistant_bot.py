'''
Консольний застосунок CLI (Command Line Interface) складається з трьох елементів:
1) Парсер команд -  розбір введених користувачем рядків, виділення з рядка ключових 
слів та модифікаторів команд.
2) Функції-обробники команд - набір функцій (handler), вони відповідають за безпосереднє 
виконання команд.
3) Цикл запит-відповідь - отримання від користувача даних та повернення користувачеві 
відповіді від функції - handler-а.
'''

'''
бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону 
за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг.
'''

welcome_banner = '''
  ___          _     _              _     _           _   
 / _ \        (_)   | |            | |   | |         | |  
/ /_\ \___ ___ _ ___| |_ __ _ _ __ | |_  | |__   ___ | |_ 
|  _  / __/ __| / __| __/ _` | '_ \| __| | '_ \ / _ \| __|
| | | \__ \__ \ \__ \ || (_| | | | | |_  | |_) | (_) | |_ 
\_| |_/___/___/_|___/\__\__,_|_| |_|\__| |_.__/ \___/ \__|
'''

commands = '''
1) hello - greet the assistant bot
2) add username phone - add a new contact with name and phone number
3) change username phone - change the phone number for an existing contact
4) phone username - show the phone number of the contact
5) all - show all saved contacts
6) help - show this help menu
7) exit or close - exit the application
'''
def init():
    print(welcome_banner)
    print(commands)
    print()

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError: # користувач ввів неправильну кількість аргументів
            return "Give me name and phone please."
        except KeyError: # намагаєшся отримати значення з словника за ключем, якого там немає
            return "User not found."
        except IndexError: # користувач не ввів аргументи для команди
            return "Enter user name."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)

@input_error
def say_hello():
    return "How can I help you?"

@input_error
def show_help():
    return commands


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Invalid command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print(say_hello())

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "help":
            print(show_help())

        else:
            print("Invalid command.")


if __name__ == "__main__":
    init()
    main()
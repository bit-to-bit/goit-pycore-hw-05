'''Main app module'''

import handler
import utils
from utils import generate_input_invite

def main():
    '''App runtime'''

    print(handler.greeting())
    while True:
        command, *args = utils.parse_input(input(generate_input_invite()))
        print()

        if command in ["close", "exit"]:
            print(handler.app_exit())
            break
        if command == "hello":
            print(handler.hello())
        elif command == "add":
            print(handler.add_contact(args))
        elif command == "change":
            print(handler.change_contact(args))
        elif command == "delete":
            print(handler.delete_contact(args))
        elif command == "phone":
            print(handler.show_phone(args))
        elif command == "all":
            print(handler.show_all())
        elif command == "demo":
            print(handler.demo())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

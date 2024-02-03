import sys

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    if name in contacts:
        return "Contact added."

def show_phone(args, contacts):
        name = args[0]
        if name in contacts:
            return contacts[name]
        return "Not found"

def change_contact(args, contacts):
    name = args[0]
    if not name in contacts:
        return "Not found"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact change"
def all_contact(contacts):
    if contacts:
        for k,v in contacts.items():
            print(f"{k} - {v}")
    else:
        return "Not found"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

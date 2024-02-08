def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Please provide name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid number of arguments. Please provide a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'

def show_all_numbers(contacts):
    if not contacts:
        return "No contacts available."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

def change_number(args, contacts, user_input):
    if len(args) !=1:
        return "Invalid number of arguments. Please provide a name."
    name = args[0]
    if name in contacts:
        contacts[name] = user_input
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)


        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_numbers(contacts))
        elif command == "change":
            user_input = input("Enter a new number: ")
            print(change_number(args, contacts, user_input))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

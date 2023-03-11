import pandas as pd


contacts = {}


def add_contact():
    name = input("Enter the name of the contact:\n")
    number = input("Enter the number of the contact:\n")
    contacts[name] = number


def remove_contact():
    name = input("enter the name of the contact you want to remove:\n")
    for key in contacts:
        if key == name:
            del contacts[key]
            break
        else:
            print("contact not found")
            remove_contact()


def search_contact():
    name = input("enter the name of the contact you want to search:\n")
    for key in contacts:
        if key == name:
            print(contacts[key])
            break
        else:
            print("contact not found")
            search_contact()


def main():
    while True:
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Search contact")
        print("4. Display contacts")
        print("5. Exit")
        choice = int(input("Enter your choice:\n"))
        if choice == 1:
            add_contact()
        elif choice == 2:
            remove_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            print(contacts)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            continue


if __name__ == "__main__":
    main()

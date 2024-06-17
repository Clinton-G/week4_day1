from contacts_manager import add_contact, remove_contact, display_contacts

def main():
    print("Welcome to the Contact Manager!")

    while True:
        print("\nMenu:")
        print('- - - - - - - - - -')
        print("1. Add a Contact")
        print("2. Remove a Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("\nEnter Input: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            add_contact(name, phone)

        elif choice == '2':
            name = input("Enter Name: ")
            remove_contact(name)

        elif choice == '3':
            display_contacts()

        elif choice == '4':
            print("Have a Good Day")
            break

        else:
            print("Invalid Input, Please Try Again")

if __name__ == "__main__":
    main()

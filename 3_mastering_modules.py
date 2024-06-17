import text_utils as utils

def main():
    print("Welcome to the Program")

    while True:
        print("\nMenu:")
        print("1. Reverse a String")
        print("2. Capitalize a String")
        print("3. Exit")

        choice = input("\nEnter Input: ")

        if choice == '1':
            rev_str = input("Enter a String to Reverse: ")
            print('Reversed Strong:', rev_str[::-1])

            
        elif choice == '2':
            cap_str = input("Enter a String to Capitalize: ")
            print('Capitalized String:', cap_str.capitalize())

        elif choice == '3':
            print("Have a Good Day")
            break

        else:
            print("Invalid Input, Please Try Again")

if __name__ == "__main__":
    main()


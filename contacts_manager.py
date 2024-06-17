contacts_list = []

def add_contact(name, phone):
    contact = {'name': name, 'phone': phone}
    contacts_list.append(contact)
    print('\n', name, 'Has Been Added')

def remove_contact(name):
    for contact in contacts_list:
        if contact['name'] == name:
            contacts_list.remove(contact)
            print('\n', name, 'Has Been Deleted')
            return
    print(name, 'Not Found')

def display_contacts():
    if contacts_list:
        print("\nContacts:")
        for contact in contacts_list:
            print('Name:', contact['name'], '-', 'Phone:', contact['phone'])
    else:
        print("No contacts found.")


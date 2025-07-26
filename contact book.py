class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added.")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("              Contact List            ")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")
    def search_contact(self):
        keyword = input("Enter name or phone to search: ").lower()
        for contact in self.contacts:
            if keyword in contact.name.lower() or keyword in contact.phone:
                print("             Contact Found             ")
                contact.display()
                return
        print("Contact not found.")
    def update_contact(self):
        name = input("Enter name of contact to update: ").lower()
        for contact in self.contacts:
            if contact.name.lower() == name:
                print("Leave field empty to keep existing value.")
                new_phone = input(f"New phone [{contact.phone}]: ") or contact.phone
                new_email = input(f"New email [{contact.email}]: ") or contact.email
                new_address = input(f"New address [{contact.address}]: ") or contact.address

                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated.")
                return
        print("Contact not found.")
    def delete_contact(self):
        name = input("Enter name of contact to delete: ").lower()
        for contact in self.contacts:
            if contact.name.lower() == name:
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")
def main():
    book = ContactBook()
    while True:
        print("                  CONTACT BOOK MENU                  ")
        print("1: Add Contact")
        print("2: View Contacts")
        print("3: Search Contact")
        print("4: Update Contact")
        print("5: Delete Contact")
        print("6: Exit")
        choice = input("Enter your choice : ")
        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            book.search_contact()
        elif choice == "4":
            book.update_contact()
        elif choice == "5":
            book.delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
main()

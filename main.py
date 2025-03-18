import csv
import os
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# File to store contacts
CONTACTS_FILE = "contacts.csv"

# Function to check if the contacts file exists; if not, create it
def initialize_file():
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address"])  # Header row

# Function to add a contact
def add_contact():
    print(Fore.CYAN + "\n📌 Add a New Contact:")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    with open(CONTACTS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, address])

    print(Fore.GREEN + f"\n✅ Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    print(Fore.YELLOW + "\n📋 Contact List:")
    
    with open(CONTACTS_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        contacts = list(reader)

    if not contacts:
        print(Fore.RED + "No contacts found!")
        return

    for i, contact in enumerate(contacts, start=1):
        print(Fore.BLUE + f"{i}. {contact[0]} - {contact[1]}")

# Function to search for a contact
def search_contact():
    search_query = input(Fore.CYAN + "\n🔍 Enter Name or Phone Number to search: ").strip()

    with open(CONTACTS_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        found_contacts = [contact for contact in reader if search_query in contact]

    if found_contacts:
        print(Fore.GREEN + "\n🔎 Search Results:")
        for contact in found_contacts:
            print(Fore.BLUE + f"📌 Name: {contact[0]}")
            print(Fore.BLUE + f"📞 Phone: {contact[1]}")
            print(Fore.BLUE + f"📧 Email: {contact[2]}")
            print(Fore.BLUE + f"🏠 Address: {contact[3]}\n")
    else:
        print(Fore.RED + "❌ No matching contacts found!")

# Function to update a contact
def update_contact():
    name_to_update = input(Fore.CYAN + "\n✏️ Enter Name of contact to update: ").strip()
    updated_contacts = []
    found = False

    with open(CONTACTS_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        contacts = list(reader)

    for contact in contacts:
        if contact[0].lower() == name_to_update.lower():
            print(Fore.YELLOW + "\n🔄 Updating Contact...")
            contact[1] = input("Enter New Phone Number: ").strip() or contact[1]
            contact[2] = input("Enter New Email: ").strip() or contact[2]
            contact[3] = input("Enter New Address: ").strip() or contact[3]
            found = True
        updated_contacts.append(contact)

    if found:
        with open(CONTACTS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(updated_contacts)
        print(Fore.GREEN + "✅ Contact updated successfully!")
    else:
        print(Fore.RED + "❌ Contact not found!")

# Function to delete a contact
def delete_contact():
    name_to_delete = input(Fore.RED + "\n🗑️ Enter Name of contact to delete: ").strip()
    updated_contacts = []
    deleted = False

    with open(CONTACTS_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        contacts = list(reader)

    for contact in contacts:
        if contact[0].lower() == name_to_delete.lower():
            deleted = True
            continue  # Skip adding this contact to the new list
        updated_contacts.append(contact)

    if deleted:
        with open(CONTACTS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(updated_contacts)
        print(Fore.GREEN + f"✅ Contact '{name_to_delete}' deleted successfully!")
    else:
        print(Fore.RED + "❌ Contact not found!")

# Function to display menu
def display_menu():
    print(Fore.CYAN + "\n📖 CONTACT BOOK MENU:")
    print(Fore.YELLOW + "1️⃣ Add Contact")
    print(Fore.YELLOW + "2️⃣ View Contacts")
    print(Fore.YELLOW + "3️⃣ Search Contact")
    print(Fore.YELLOW + "4️⃣ Update Contact")
    print(Fore.YELLOW + "5️⃣ Delete Contact")
    print(Fore.YELLOW + "6️⃣ Exit")

# Main program loop
def main():
    initialize_file()
    
    while True:
        display_menu()
        choice = input(Fore.BLUE + "\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(Fore.MAGENTA + "\n👋 Exiting Contact Book. Have a great day!")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice! Please select a valid option.")

# Run the contact book program
if __name__ == "__main__":
    main()

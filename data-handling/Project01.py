import csv
import os


FILENAME = "contacts.csv"


if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline='',encoding="utf") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name:").strip()
    phone = input("Phone:").strip()
    email = input("Email:").strip()

    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contacts name already exists")
                return
            
    with open(FILENAME, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Conatct added")


def view_contacts():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows)<=1:
            print("No Contacts to show")
            return
        
        print("\n Your contacts: \n")
        
        for row in rows[0:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        found=False
        name=input("Enter Person's Name").strip().lower()
        for row in rows:
            if row["Name"].strip().lower() == name:
                print("Contact Found!")
                print(row)
                found=True
                break
        if found==False:
            print("Contact Doesn't Found!")
        
        
    
def main():

    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4)").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our software")
            break
        else:
            print("Invalid choice of number")


if __name__ == "__main__":
    main()
            

contact = {}
print("\n====My Contact-Book====")

def display_contact():
    print("\n===============================")
    print("Name\t\tContact Number")
    print("===============================")

    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input("\n1.Add new contact\n2.Search contact\n3.Display contact\n4.Edit contact\n5.Delete contact\n6.Exit\nEnter your choice: "))
    if choice == 1:
        name = input("Enter the Contact name: ")
        phone = input("Enter the Mobile number: ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the Contact name: ")
        if search_name in contact:
            print("\n===============================")
            print(search_name,"'s contact number is ",contact[search_name])
            print("================================")
        else:
            print("\n===============================")
            print("Name not found")
            print("===============================")

    elif choice == 3:
        if not contact:
            print("\n===============================")
            print("Empty Contact book")
            print("===============================")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact name to be edited: ")
        if edit_contact in contact:
            phone = input("Enter Mobile Number: ")
            contact[edit_contact] = phone
            print("\n===============================")
            print("Contact Updated")
            print("===============================")
            display_contact()
        else:
            print("\n===============================")
            print("Name not found")
            print("===============================")
    elif choice == 5:
            del_contact = input("Enter the contact name to be deleted: ")
            if del_contact in contact:
                confirm = input("Do you want to delete this Contact y/n?").lower()
                if confirm == "y":
                    contact.pop(del_contact)
                display_contact()
            else:
                print("\n===============================")
                print("Name not found")
                print("===============================")
    elif choice == 6:
        break
    else:
        print("\n===============================")
        print("Invalid Input")
        print("===============================")










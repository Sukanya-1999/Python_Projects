contacts ={}

while True:
    print('\n Contact Book App')
    print('1, Create Contact')
    print('2, View Contact')
    print('3, Update Contact')
    print('4, Delete Contact')
    print('5, Search Contact')
    print('6, Count Contact')
    print('7, Exit')
    

    choice = input("Enetr your choice = ")
    if choice == '1':
        name = input('Enter your name =')
        if name in contacts:
            print(f'Conatct name {name} already exists!')
        else:
            age = input("Enetr age = ")    
            email = input("Enetr email = ")    
            mobile = input("Enetr mobile number = ") 
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile} 
            print(f'Contact name {name} has been created successfully')

    elif choice == '2':
        name = input("Enter contact name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name}, Age:{age}, Mobile:{mobile}')
        else:
            print('Contact not found') 

    elif choice == '3':
        name = input("Enter contact name to update contact = ")
        if name in contacts:
            age = input("Enetr updated age = ")    
            email = input("Enetr updated email = ")    
            mobile = input("Enetr updated mobile number = ") 
            contact[name] = {'age':int(age), 'email':email, 'mobile':mobile} 
        
        else:
            print('Contact not found')

    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully')

        else:
            print('Contact not found') 


    elif choice == '5':
        search_name = input('Enter the name you want to search in list =') 
        found = False 
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'found Name {name}, Age {age}, Mobile Number:{mobile}, Email:{email}')
                found = True

        if not found:
            print('No contact found with this name')


    elif choice == '6':
        print(f'Total conatcts in your book : {len(contacts)}')

    elif choice == '7':
        print('Closing the program')
        break

    else:
        print('Invalid input') 

if __name__ == "__main__":
    main()                               
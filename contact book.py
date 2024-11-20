#empty dictionary
contacts={}
while True:
    print("contact book")
    print("1 create contact")
    print("2 view contact")
    print("3 update contact")
    print("4 delete contact")
    print("5 search contact")
    print("6 count contact")
    print("6 exit")

    choice=int(input("enter number to perform operation:"))
    if choice==1:
        name=input("enter name")
        if name in contacts:
            print(f"{name} already exist")
        else:
            age=input("enter age")
            email=input("enter email")
            address=input("enter address")
            contacts[name]={"age":age,"emal":email,"address":address}
            print(f"contact of name {name} has been created successfully")
    elif choice==2:
        name=input("enter contact name")
        for name in contacts:
            if name in contacts:
                #contact=contacts[name]
                print(f" name:{name}, age:{age},emial:{email}, address:{address}")
            #print(f"you contact name {name} has been updated")
        else:
            print("contact not found")
    elif choice==3:
        name=input("enter name")
        if name in contacts:
            age=int(input("enter newage"))
            email=input("enter new email")
            address=input("enter new address")
            contacts[name]=("age:{age},emial:{email}, address:{address}")
            print(f"you contact name {name} has been updated")
        else:
            print("contact not found")

    elif choice==4:
        name=input("enter name")
        if name in contacts:
            del contacts[name]
            print(f"your contact name {name} has been deleted")
        else:
            print("contact not found")
    elif choice==5:
        name=input("enter name")
        for name in contacts:
            if name in contacts:
                print (f"age:{age},emial:{email}, address:{address}")
            else:
                print("not found")
    elif choice==6:
        print(f"the total contact is {len(contacts)}")
    else:
        exit
            

            








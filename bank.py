# Source Code

print("\t\t\t***** BankWithUs *****")

bank_data = {}

while True:
    print("\n\n\t\t\t----- Main Menu -----")
    ch = int(input("\n\n1.New Customer\n2.Existing Customer\n3.Exit\n\nEnter choice:"))

    if ch == 1:
        name = input("\nEnter name:")
        city = input("Enter city:")
        age = int(input("Enter age:"))
        acc = input("Enter account type:")
        amt = int(input("Enter amount:"))
        acc_no = int(input("Enter account no:"))
        
        user_data = {}
        user_data["name"] = name
        user_data["city"] = city
        user_data["age"] = age
        user_data["account"] = acc
        user_data["amount"] = amt
        bank_data[acc_no] = user_data

        print("\nACCOUNT CREATED\n")

    elif ch == 2:
        acc_no = int(input("Enter account no:"))
        if acc_no in bank_data:
            print("\nACCOUNT EXISTS\n")

            while True:
                print("\n\n\t\t\t----- User Portal -----")
                choice = int(input("\n1.Check Balance\n2.Withdraw\n3.Deposit\n4.Back to main menu\n\nEnter choice:"))

                if choice == 1:
                    print("\nYour available balance:",bank_data[acc_no]["amount"])
                    
                elif choice == 2:
                    withd = int(input("\nEnter withdraw amount:"))
                    bank_data[acc_no]["amount"] = bank_data[acc_no]["amount"] - withd
                    print("\nAmount withdrawn, now your available balance is %i"%bank_data[acc_no]["amount"])
                    
                elif choice == 3:
                    dep = int(input("\nEnter deposit amount:"))
                    bank_data[acc_no]["amount"] = bank_data[acc_no]["amount"] + dep
                    print("\nAmount deposited, now your available balance is %i"%bank_data[acc_no]["amount"])

                elif choice == 4:
                    break

                else:
                    print("\n\nINVALID CHOICE!")
                
        else:
            print("\nACCOUNT NOT FOUND\n")
            
    elif ch == 3:
        break
    else:
        print("\n\nINVALID CHOICE!")

print("\n\n***** Thank you for banking with us *****")

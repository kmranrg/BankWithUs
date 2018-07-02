# Source Code

print("\t\t\t***** BankWithUs *****")

bank_data = {}
user_data = {}

while True:
    
    ch = int(input("\n\n1.New Customer\n2.Existing Customer\n3.Exit\n\nEnter choice:"))

    if ch == 1:
        name = input("\nEnter name:")
        city = input("Enter city:")
        age = int(input("Enter age:"))
        acc = input("Enter account type:")
        amt = int(input("Enter amount:"))
        acc_no = int(input("Enter account no:"))

        user_data["name"] = name
        user_data["city"] = city
        user_data["age"] = age
        user_data["account"] = acc
        user_data["amount"] = amt
        bank_data[acc_no] = user_data

        print("\nACCOUNT CREATED")
        print(bank_data)
        
        

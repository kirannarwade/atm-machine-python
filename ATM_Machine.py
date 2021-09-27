import time

print("Enter Your Card")

time.sleep(3)

print("Welcome To Kiran Bank LTD")

password = 1234

pin = int(input("Enter Your Pin Here: "))

balance = 10000

if pin == password:
    while True:
        print('''
        1 . Balance 
        2 . Withdraw
        3 . Deposit
        4 . Exit
        '''
        )

        try:
            option = int(input("Enter your choice: "))
        except:
            print("Invalid Keyword")    

        if option == 1:
            print(f"Your Current Balance of RS.{balance}") 

        elif option == 2:
            withdraw_amt = int(input("Enter amount to withdraw: ")) 
            if withdraw_amt > balance:
                print("Insufficient Balance")    
            else:  
                balance = balance - withdraw_amt
                print(f"{withdraw_amt}.Rs is debited in your account")
                print(f"Your Updated Balance of RS.{balance}")

        elif option == 3:
            deposit_amt = int(input("Enter amount to deposit: "))        
            balance = balance + deposit_amt
            print(f"{deposit_amt}.Rs is credited in your account")
            print(f"Your updated balance of RS.{balance}")

        elif option > 4:
            print("Invalid Choice please enter correct")

        elif option == 4:
            print("Thank you for visiting, Have a nice day.")    
            break



else:
    print("Incorrect Pin")
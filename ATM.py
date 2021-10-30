print("WELCOME")
insert_card=input("enter your card")
if insert_card=="credit" or insert_card=="debit":
    print("process")
    language=input("please select language")
    if language=="hindi"or"english":
        print(language)
        enter_pin=int(input("please enter your 4 digit pin"))
        if enter_pin<=10000:
            print("pin entered")
            type_of_acc=input("select the type of account")
            if type_of_acc=="saving":
                print("your accout is a saving account") 
                cash_withdrawl=int(input("please choose 'BANKING'for cash withdrawl"))
                if cash_withdrawl<=15000:
                   print("please collect your money and take a printed receipt")
                   balance=int(input("check your balence "))
                   if balance==50000:
                       print("50000 available on your aacount")
                       receipt=input("do you have your receipt")
                       if receipt=="yes":
                           print("please you take your receipt")
                       else:
                            print("not take receipt")
                else:
                    print("not collect money")
            else:
                print("your account is invalid")
        else:
            print("pin not entered")
    else:
        print("plese select language first")
else:
    print("failed")
                   





day=input("enter the day")
disco=input("enter the permission")
if day=="Sunday":
    if disco=="ok":
        print("yes you can go anywhere")
elif day=="monday":
    if disco=="ok":
        print("where are you go")
        place=input("enter the place")
        if place=="hospital":
            work=input("what work")
            if work=="healthissue":
              print("yes you can go but you are quarantine for 7 days")
        elif place=="hill":
            work=input("what work")
            if work=="roaming":
                 print('not allowed')
        elif place=="market":
            work=input("why")
            if work=="shopping":
                print('Ok you can go,you are vaccinated,but you are quarantine for 1 day')
            else:
                print("only vaccinated people go outside")  
        else:
            print("without vaccination not allowed to go outside")
    else:
         print("not go outside") 
else:
    ("no you cann't go outside")     
        
        
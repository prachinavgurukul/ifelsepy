leap_year=int(input("enter the leap year"))
if leap_year%4==0:
    if leap_year%100==0:
        if leap_year%400==0:
            print("leapyear",leap_year)
        else:
            print("not leapyear",leap_year)
    else:
     print("leap year")
else:
    print("not a leap year")



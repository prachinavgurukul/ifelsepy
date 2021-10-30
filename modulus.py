disco=input("take permission from disco")
day=input("enter the day")
if day=="monday"or"tuesday"or"wednessday"or"thrusday"or"friday":
    print("you cann't go outside")
    place=input("enter the place")
    disease=input('enter the disease')
    if place=="hospital":
        if disease=="heartproblem"or"cheastpain":
           print("yes you can go")
        else:
            print("you cann't go")
elif day=="sunday":
    print("yes you can go anywhere")
else:
    print("you cann't go anywhere")